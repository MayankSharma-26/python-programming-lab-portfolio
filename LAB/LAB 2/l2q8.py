cost = float(input("Enter the cost : "))
revenue = float(input("Enter the revenue : "))
if cost==revenue:
    print("Break Even")
elif revenue>cost:
    print("Profit")
else:
    print("Loss")