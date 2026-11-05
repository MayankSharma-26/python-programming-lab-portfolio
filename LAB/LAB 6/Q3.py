# n = int(input("ENTER YOUR NO: "))
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# n = int(input("ENTER YOUR NO: "))
# i=1
# while i <=n:
#     j=0
#     while j<i:
#         print("*", end=" ")
#         i+=1
#         j+=1

# n = int(input("ENTER YOUR NO: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*", end=" ")
#         j+=1
#     print()
#     i+=1

# n = int(input("ENTER YOUR NO: "))
# i = 1
# while i <= n:
#     j=1
#     while j<=n-i:
#         print(" ", end=" ")
#         j+=1
#     j=1
#     while j<=i:
#         print("*", end=" ")
#         j+=1
#     print()
#     i+=1


n = int(input("ENTER YOUR NO:"))
i=1
for i in range (1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
# n = int(input("ENTER YOUR NO: "))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ", end=" ")
#         j += 1
#     j = 1
#     while j <= 2*i-1:
#         print("*", end=" ")
#         j += 1
#     print()
#     i+=1
