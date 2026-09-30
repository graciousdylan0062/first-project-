
expenses = []
total = 0
running = True

while running:
    amount = float(input("Enter the amount (0 to stop): "))
    if amount == 0:
        running = False
    else:
        expenses.append(amount)
        total += amount

print("Total:", total)
print("Expenses:", expenses)