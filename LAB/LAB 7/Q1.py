n=int(input("ENTER HOW MANY NO: "))
sum=0
for i in range(1, n+1):
    sum=sum+1/i
print(f"sum = {sum:.9f}")

# n=int(input("ENTER HOW MANY NO: "))
# fac=1
# sum=0
# for i in range (1,n+1):
#      fac=i*fac
#      sum=sum+1/fac
# print(f"sum={sum:.9f}")

# n=int(input("ENTER HOW MANY NO: "))
# sum=0
# for i in range (1,n+1):
#     if i%2==0:
#         sum=sum-1/i**2
#     else:
#         sum=sum+1/i**2
# print(f"sum={sum:.9f}")