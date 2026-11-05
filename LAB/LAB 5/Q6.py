# n = int(input("Enter N: "))
# firstno = 1
# second_to_add = 1
# for i in range(n):
#     print(firstno, end=" ")
#     c = firstno + second_to_add
#     firstno = second_to_add
#     second_to_add = c

n = int(input("Enter N: "))
firstno = 1
second_to_add = 1
sum=0
for i in range(n-1):
    sum=firstno+sum
    c = firstno + second_to_add
    firstno = second_to_add
    second_to_add = c
print(sum)

    