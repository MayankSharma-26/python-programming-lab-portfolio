a=int(input("Enter Hours"))
b=int(input("Enter Minutes"))
if a>=0 and a<=23 and b>=0 and b<=59:
    b=b+15
    if b>=60:
        b=b-60
        a=a+1
        if a>=24:
            a=a-24
    print("Time after 15 minutes is",a,":",b)
else:
    print("Invalid Time")
