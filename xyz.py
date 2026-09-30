#calculator

a = float(input("value of a: "))
b = float(input("value of b: "))

op = input("choose operation (+,-,*,/): ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("infinity")
        result = None
    else:
        result = a / b
else:
    print("error")
    result = None

if result is not None:
    print("Result:", result)
