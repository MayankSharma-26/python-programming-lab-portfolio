num = int(input("Enter a 3-digit number: "))
h = num // 100         
t = (num // 10) % 10   
o = num % 10   
total = h**3 + t**3 + o**3
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
    
    