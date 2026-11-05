S= int(input("Enter Your Gross Salary:"))
if S<=300000:
    print("Your Tax is 0%")
elif 300000>S<=1000000:
    print("Your Tax is 10%")
elif 1000000>S<=2500000:
    print("Your Tax is 20%")
else:
    print("Your Tax is 30%")    