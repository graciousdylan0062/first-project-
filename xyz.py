# Simple command-line calculator

try:
    a = float(input("Value of a: "))
    b = float(input("Value of b: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    op = input("Choose operation (+, -, *, /): ").strip()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            result = None
            print("Cannot divide by zero.")
        else:
            result = a / b
    else:
        result = None
        print("Unsupported operation. Choose +, -, *, or /.")

    if result is not None:
        print("Result:", result)
