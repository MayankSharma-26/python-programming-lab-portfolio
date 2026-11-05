a = int(input("Press 1 for Square\nPress 2 for Rectangle\nPress 3 for Circle\nPress 4 for Triangle\n"))
if a ==1:
    s=int(input("Enter Side of square:"))
    sarea=s*s
    print(sarea)
elif a==2:
    l=int(input("Enter Length of Rectangle"))
    b=int(input("Enter Breadth Of Rectangle"))
    sarea=l*b
    print(sarea)
elif a==3:
    r=int(input("ENter Radius Of Circle"))
    sarea=3.14*r**2
    print(sarea)
elif a==4:
    ba=int((input("Enter Bse of Triangle")))
    h=int(input("Enter Height Of Triangle"))
    sarea=0.5*ba*h
    print(sarea)
else:
    print("Invalid Input")
    