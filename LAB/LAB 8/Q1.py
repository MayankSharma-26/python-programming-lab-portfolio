# r=int(input("ENTER ROWS"))
# c=int(input("ENTER COLOUMS"))
# for i in range (0,r):
#     print("*", end="")
#     for j in range(0,c):
#         print("*", end="")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()