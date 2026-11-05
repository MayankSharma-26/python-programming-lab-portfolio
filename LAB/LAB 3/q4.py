n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
    if sum%3==0:
        print("sum of digits is div by 3")
print("Sum of digits:", sum)