n = int(input("Enter Your No = "))
if n <= 1:
    print("NO is NOT PRIME")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("NO is PRIME")
    else:
        print("NO is NOT PRIME")