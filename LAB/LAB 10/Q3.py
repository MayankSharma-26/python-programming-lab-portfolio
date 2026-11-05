# def cf(list1):
#     list1=list(map(int,input("ENTER ELEMETS:").split()))
#     l=int(input("ENTER NO WANT TO SHIFT:"))
#     for i in range(l):
#         a=list1.pop(0)
#         list1.append(a)
#     print(list1)
   
# list1=int(input("ENTER NO OF ELEMENTS:")) 
# print(cf(list1))

# def cf(list1):
#     l = int(input("ENTER NO WANT TO SHIFT:"))
#     for i in range(l):
#         a = list1.pop(0)
#         list1.append(a)
#     return list1
# list1 = list(map(int, input("ENTER ELEMENTS:").split()))  '''list1 = list(map(int, input("ENTER ELEMENTS:").split()))'''
# print(cf(list1))

def cf(list1):
    l = int(input("ENTER NO WANT TO SHIFT:"))
    s=int(input("ENTER WHERE TO SHIFT\n 1=LEFT\n2=RIGHT:"))
    if s==1:
        for i in range(l):
                a = list1.pop(0)
                list1.append(a)
        return list1
    elif s==2:
        for i in range(l):
            a = list1.pop()
            list1.insert(0, a)
        return list1
    else:
        return "INVALID INPUT"
# list1 = list(map(int, input("ENTER ELEMENTS:").split()))  #list1 = list(map(int, input("ENTER ELEMENTS:").split()))
list1=[]
x=int(input("ENTER NO OF ELEMENTS:"))
for i in range (x):
    p=int(input("ENTER ELEMENT:"))
    list1.append(p)
print(cf(list1))