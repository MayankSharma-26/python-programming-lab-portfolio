msg=input("ETNER YOUR STRING:").lower()
key=int(input("ENTER YOUR KEY:"))
r=""
msg=msg.replace(" ","")
for i in msg:
    a=ord(i)+key
    if a>122:
        a=(a-26)
    elif a<97:
        a=(a+26)
    r=r+chr(a)
print(r)