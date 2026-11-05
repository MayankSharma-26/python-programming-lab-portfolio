x = input("Enter a string: ")
rev = ""
for i in range(len(x)-1,-1,-1):
    rev=rev+x[i]
if x==rev:
    print("Palindrome")
else:
    print("Not a palindrome")