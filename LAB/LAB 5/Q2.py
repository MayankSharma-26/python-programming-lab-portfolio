# n = int(input("Enter a positive integer: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
# print(sum)


n = input("Enter a positive integer: ")
digit_sum = 0
for i in n:
    digit_sum += int(i)
print(digit_sum)

