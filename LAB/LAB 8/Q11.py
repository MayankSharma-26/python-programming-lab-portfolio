# n=int(input("ENTER NO"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         a=i%j
#         if a==0:
#             print(i)

# n = int(input("ENTER YOUR NUMBER:"))
# for i in range(1, n + 1):
#     print("Factors of", i, ":", end=" ")
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print(j, end=" ")

#     print()
n = int(input("ENTER YOUR NUMBER:"))
for i in range(1, n + 1):
        print("Factors of", i, ":", end=" ")
        for j in range(1, i + 1):
            if i % j == 0:
                print(j, end=" ")
        print()