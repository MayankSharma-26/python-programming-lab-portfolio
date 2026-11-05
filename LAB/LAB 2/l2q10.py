pounds = float(input("Enter  in pounds: "))
cash = float(input("Enter cash in dollars: "))
total = pounds * 2.50
if cash >= total:
    change = cash - total
    print("Change to be returned: $", change)
else:
    owed = total - cash
    print("Amount owed: $", owed)