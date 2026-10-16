
import sqlite3
from pathlib import Path

import streamlit as st

# ---------- App configuration ----------

st.set_page_config(
    page_title="Study Planner",
    page_icon="📚",
    layout="wide",
)

DB_PATH = Path(__file__).parent / "study_planner.db"


# ---------- Database setup ----------

def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject_id INTEGER NOT NULL,
                due_date TEXT NOT NULL,
                priority TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (subject_id) REFERENCES subjects(id)
            )
        """)


initialize_database()


# ---------- Page heading ----------

st.title("📚 My Study Planner")
st.caption("Plan smarter. Stay consistent. Make progress.")

page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Subjects", "Tasks"],
)


# ---------- Subjects page ----------

if page == "Subjects":
    st.header("My Subjects")

    with st.form("add_subject", clear_on_submit=True):
        subject_name = st.text_input("Subject name")
        submitted = st.form_submit_button("Add subject")

        if submitted:
            name = subject_name.strip()

            if not name:
                st.error("Please enter a subject name.")
            else:
                try:
                    with get_connection() as connection:
                        connection.execute(
                            "INSERT INTO subjects (name) VALUES (?)",
                            (name,),
                        )
                    st.success(f"Added {name}!")
                    st.rerun()
                except sqlite3.IntegrityError:
                    st.warning("That subject already exists.")

    with get_connection() as connection:
        subjects = connection.execute(
            "SELECT id, name FROM subjects ORDER BY name"
        ).fetchall()

    if subjects:
        for subject_id, name in subjects:
            st.write(f"📘 {name}")
    else:
        st.info("No subjects yet. Add your first one above.")


# ---------- Tasks page ----------

elif page == "Tasks":
    st.header("My Tasks")

    with get_connection() as connection:
        subjects = connection.execute(
            "SELECT id, name FROM subjects ORDER BY name"
        ).fetchall()

    if not subjects:
        st.info("Add a subject first, then come back to create tasks.")
    else:
        subject_options = {name: subject_id
                           for subject_id, name in subjects}

        with st.form("add_task", clear_on_submit=True):
            title = st.text_input("Task or assignment")
            subject_name = st.selectbox(
                "Subject", list(subject_options.keys())
            )
            due_date = st.date_input("Due date")
            priority = st.selectbox(
                "Priority", ["Low", "Medium", "High"]
            )

            submitted = st.form_submit_button("Save task")

            if submitted:
                if not title.strip():
                    st.error("Please enter a task title.")
                else:
                    with get_connection() as connection:
                        connection.execute(
                            """
                            INSERT INTO tasks
                            (title, subject_id, due_date, priority)
                            VALUES (?, ?, ?, ?)
                            """,
                            (
                                title.strip(),
                                subject_options[subject_name],
                                due_date.isoformat(),
                                priority,
                            ),
                        )
                    st.success("Task saved!")
                    st.rerun()

        st.subheader("Task list")

        with get_connection() as connection:
            tasks = connection.execute("""
                SELECT tasks.id, tasks.title, subjects.name,
                       tasks.due_date, tasks.priority, tasks.completed
                FROM tasks
                JOIN subjects ON subjects.id = tasks.subject_id
                ORDER BY tasks.due_date, tasks.id
            """).fetchall()

        if not tasks:
            st.info("No tasks yet.")
        else:
            for task_id, title, subject, due, priority, completed in tasks:
                with st.container(border=True):
                    col1, col2 = st.columns([4, 1])

                    with col1:
                        st.write(f"**{title}**")
                        st.caption(
                            f"{subject} · Due {due} · {priority} priority"
                        )

                    with col2:
                        is_done = st.checkbox(
                            "Completed",
                            value=bool(completed),
                            key=f"task_{task_id}",
                        )

                        if is_done != bool(completed):
                            with get_connection() as connection:
                                connection.execute(
                                    "UPDATE tasks SET completed = ? "
                                    "WHERE id = ?",
                                    (int(is_done), task_id),
                                )
                            st.rerun()


# ---------- Dashboard page ----------

else:
    st.header("Your Progress")

    with get_connection() as connection:
        total_subjects = connection.execute(
            "SELECT COUNT(*) FROM subjects"
        ).fetchone()[0]

        total_tasks, completed_tasks = connection.execute(
            """
            SELECT COUNT(*), COALESCE(SUM(completed), 0)
            FROM tasks
            """
        ).fetchone()

    percentage = (
        completed_tasks / total_tasks if total_tasks else 0
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Subjects", total_subjects)
    col2.metric("Total tasks", total_tasks)
    col3.metric("Completed", completed_tasks)

    st.subheader("Task completion")
    st.progress(percentage)
    st.write(f"{percentage:.0%} of your tasks completed.")

    if total_tasks == 0:
        st.info("Start by adding a subject and creating a task.")
