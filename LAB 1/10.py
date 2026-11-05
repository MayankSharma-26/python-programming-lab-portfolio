seconds = int(input("Enter seconds: "))
if seconds < 1 or seconds > 86400:
    print("Invalid input")
else:
    hours=seconds//3600
    remaining=seconds%3600
    minutes=remaining//60
    seconds=remaining % 60
    print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
'''take input from user
if input is <1 or seconds > 86400
print invalid input
else 
hours =second // 3600
remaining = seconds % 3600'''