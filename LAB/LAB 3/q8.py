P = float(input("Enter monthly saving amount: "))
N = int(input("Enter number of months: "))
r = 0.05 / 12
if P <= 0:
    print("Invalid monthly saving amount.")
elif N <= 0:
    print("Invalid number of months.")
else:
    A = P * (((1 + r) ** N - 1) / r) * (1 + r)
    print("Account value after", N, "months =", round(A, 2))