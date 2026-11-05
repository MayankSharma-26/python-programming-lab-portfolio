import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    print("Invalid input: This is not a quadratic equation.")
else:
    d = b**2 - 4*a*c
    if d < 0: 
        print("No real solutions.")
    elif d == 0:
        x = -b / (2*a)
        print("The solution is:",x)
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"The solutions are: x1 = {x1:.2f}, x2 = {x2:.2f}")