income = int(input("Enter your income: "))
if income <= 20000:
    tax = income * 0.02
elif income <= 50000:
    tax = (income - 20000) * 0.025 + 400
else:
    tax = (income - 50000) * 0.03 + 1150
print("Your taxable income is:", tax)