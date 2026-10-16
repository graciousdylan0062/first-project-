import random

def play_game():
    select_number = random.randint(1, 10)
    attempts = 0

    print("\nHello human! Welcome to Number Guess!")
    print("Guess a random number from 1 to 10.\n")

    while True:
        guess = int(input("Enter the number: "))
        attempts += 1

        if guess == select_number:
            print(f"Congratulations! You guessed the number in {attempts} attempt(s)!")
            break
        elif guess < select_number:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")

    print(f"The correct number was: {select_number}")
    return attempts

# ---------- Main loop ----------

total_games = 0
total_attempts = 0

while True:
    attempts = play_game()
    total_games += 1
    total_attempts += attempts

    print(f"\nScore - Games played: {total_games} | Total attempts: {total_attempts} | Avg attempts: {total_attempts / total_games:.1f}")

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("\nThanks for playing! Goodbye!")
        break