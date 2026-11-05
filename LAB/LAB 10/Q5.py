# def isp():
#     x=int(input("ENTER STARTING OF RANGE:"))
#     y=int(input("ENTER END OF RANGE:"))
#     count=0
#     for i in range (x,y+1):
#         for j in range (1,i+1):
#             if j % i == 0:
#                 return i 
#                 count=count+i
#             return sum
# print(isp())


#---------------------------------- sir kya return loop rok deta h?

def isp(x, y):
    total = 0
    for i in range(x, y + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            print(i)
            total += i
    return total
x = int(input("ENTER STARTING OF RANGE: "))
y = int(input("ENTER END OF RANGE: "))

print("Sum:", isp(x, y))