x=int(input("Enter a Number: "))
y=int(input("Enter Other Number: "))
N=int(input("Enter Your main no.: "))
for i in range (x, y+1):
    if i%N==0:
        print(i)
        i+=1
    else:
        continue