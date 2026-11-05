num1=int(input("Enter FIrst NUMBER:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter THird Number:"))
if num1+num2 > num3:
    print("Triangle can be formed")
elif num1+num3>num2:
    print("Triangle can be Formed")
elif num2+num3>num1:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
    