# a=int(input("Enter a postive int:  "))
# pal=0
# while a>0:
#     pal=a%10
#     digit=pal
#     xm =a//10
#     if xm==a:   
#         print("palandrom")
#     else:
#         print ("not palndrom")
        
        
        
n = int(input("Enter a number: "))
no = n
pal = 0
for i in range(len(str(n))):
    digit = n % 10
    pal = pal * 10 + digit
    n //= 10
if no == pal:
    print("Palindrome")
else:
    print("Not Palindrome")