weidth = int(input("Enter number of Widget Order:"))
if weidth <= 100:
    cost = weidth * 0.25
    print("Cost of Order:", cost)
else:
    cost = weidth * 0.20
    print("Cost of Order:", cost)