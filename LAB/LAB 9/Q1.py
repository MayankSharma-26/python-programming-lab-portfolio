# 1. Write a program to reverse a string without using inbuilt function.
def srev():
    x=input("ENTER YOUR STRING:")
    a=""
    for i in range (len(x)-1,-1,-1):
        a=a+x[i]
    return a
print(srev())
    