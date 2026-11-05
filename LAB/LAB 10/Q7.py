# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
# n = int(input("Enter a number: "))
# print("Factorial =", fac(n))



# ---------------------------------------------------------

# def sum1(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum1(n - 1)
# n = int(input("Enter N: "))
# print("Sum =", sum1(n)) 

# Negative no me error hoga 

# def sum1(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum1(n - 1)
# n = int(input("Enter N: "))
# if n < 1:
#     print("Enter a positive integer")
# else:
#     print("Sum =", sum1(n))
    
# -----------------------------------------------------------

def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci(n - 1, b, a + b)
n = int(input("Enter number of terms: "))
fibonacci(n)

