# Python Beginner Projects

A collection of small Python programs built while learning programming fundamentals.

## Projects

### 1. Calculator — `xyz.py`

A command-line calculator that accepts two numbers and an operator (`+`, `-`, `*`, or `/`) and prints the result.

**Run it:**

```bash
python3 xyz.py
```

**Try these cases:**
- `10`, `5`, `+` → result should be `15.0`
- `10`, `5`, `/` → result should be `2.0`
- `10`, `0`, `/` → should handle division by zero without crashing
- Enter an unsupported operator → should report an error

### 2. Voting Eligibility Checker — `python/xyz.py`

Checks whether a person is old enough to vote. It also handles non-numeric input and negative ages.

**Run it from the repository root:**

```bash
python3 python/xyz.py
```

**Try these cases:**
- `18` → eligible to vote
- `17` → not eligible yet
- `0` → not eligible yet
- `-1` → age cannot be negative
- `hello` → asks for a whole number instead of crashing

## Requirements

- Python 3
- A terminal (macOS Terminal works)

No third-party packages are required.

## Run a project

1. Clone or download this repository.
2. Open Terminal and change into the project folder.
3. Run the command shown under the project you want to try.

## Learning goals

These projects practise:
- Variables and user input
- Converting strings to numbers
- `if / elif / else` conditions
- Arithmetic operators
- Handling invalid input with `try / except`

## Status

Beginner learning projects. They are being improved as I practise Python and add tests.
