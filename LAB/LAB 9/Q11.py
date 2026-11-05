x=input("ENTER YOUR STRING: ")
d=0
a=0
up=0
lo=0
special=0
for i in x:
    if i.isdigit():
        d+=1
    elif i.isalpha():
            a+=1
            if i.isupper():
                up+=1
            else:
                lo+=1
    elif i==" ":
        continue
    else:
        special+=1
print(d)
print(a)
print(up)
print(lo)
print(special)