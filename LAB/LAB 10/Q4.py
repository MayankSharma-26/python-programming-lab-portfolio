# def calculator(x,y):

#     user=input("ENTER YOU OPERATATION\nADD\nMINUS\nMULTIPLY\nDIVIDE").lower()
#     if user=="add":
#         a= x + y 
#         return a
#     elif user== "minus":
#         b= x- y
#         return b
#     elif user== "multiply":
#         c= x*y
#         return c
#     elif user == "divide":
#         d= x/y
#         return d
#     else:
#         return "ENTER VAILID OPERATION"
# x=int(input("ENTER NO1:"))
# y= int(input("ENTER NO2:"))
# print(calculator(x,y))


def calculator():
    x = int(input("ENTER NO1: "))
    y = int(input("ENTER NO2: "))
    user = input("ENTER OPERATION (ADD/MINUS/MULTIPLY/DIVIDE): ").lower()
    if user == "add":
        return x + y
    elif user == "minus":
        return x - y
    elif user == "multiply":
        return x * y
    elif user == "divide":
        return x / y
    else:
        return "ENTER VALID OPERATION"
print(calculator())
