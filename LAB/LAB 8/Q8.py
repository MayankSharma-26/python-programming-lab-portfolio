n = int(input("ENTER NO"))
for i in range(1, n + 1):
    for j in range(1, 11):
        if i * j % 2 == 0:
            print(i, "x", j, "=", i * j)
    print("...........")
    
    