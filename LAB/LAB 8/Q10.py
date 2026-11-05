# a = int(input("ENTER NO:"))
# b = int(input("ENTER SECOND NO:"))
# for i in range(a, b + 1):
#     prime = True
#     for j in range(2, i):
#         if i%j==0:
#             prime = False
#             break
#     if prime and i >= 2:
#         print(i, end=",")
        
a = int(input("ENTER NO:"))
b = int(input("ENTER NO 2:"))
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        print(i, end=" ")