# Voting eligibility checker

age_text = input("Enter your age: ")

try:
    age = int(age_text)
except ValueError:
    print("Please enter a whole number for your age.")
else:
    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")
