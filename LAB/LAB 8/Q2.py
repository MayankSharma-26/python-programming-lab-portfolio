rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(1, cols+1):
        print(j, end=" ")
    print()