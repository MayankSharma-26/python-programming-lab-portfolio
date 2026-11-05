# n=int(input("ENTER YOUR NO"))
# for i in range (n+1):
#     for j in range(i)
    
    
n = int(input("ENTER VALUE"))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()