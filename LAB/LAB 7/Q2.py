# x = float(input("Enter x: "))
# eps = float(input("Enter positive error: "))
# F = 0
# n = 1
# while True:
#     term = (1 / 2) ** n
#     F_new = F + term
#     if abs(F_new - F) < eps:
#         F = F_new
#         break
#     F = F_new
#     n += 1
# print("F(x) =", F)
# print("Minimum number of terms =", n)


# import math

# x = float(input("Enter x: "))
# eps = float(input("Enter positive error: "))
# F = 0
# n = 0
# while True:
#     term = ((-1) ** n) * (x ** (2*n + 1)) / math.factorial(2*n + 1)
#     F_new = F + term
#     if abs(F_new - F) < eps:
#         F = F_new
#         break
#     F = F_new
#     n += 1

# print("F(x) =", F)
# print("Minimum number of terms =", n + 1)


import math

x = float(input("Enter x: "))
eps = float(input("Enter positive error: "))

F = 0
n = 0

while True:
    term = ((-1) ** n) * (x ** (2*n)) / math.factorial(2*n)
    F_new = F + term

    if abs(F_new - F) < eps:
        F = F_new
        break

    F = F_new
    n += 1

print("F(x) =", F)
print("Minimum number of terms =", n + 1)