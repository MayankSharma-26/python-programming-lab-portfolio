holidays = int(input("Enter number of holidays: "))
workdays = 365 - holidays
total_minutes = workdays * 63 + holidays * 127
if total_minutes < 30000:
    difference = 30000 - total_minutes
    print("Tom sleeps well")
    print("Difference:", difference, "minutes")
else:
    difference = total_minutes - 30000
    print("Tom will not sleep well")
    print("Difference:", difference, "minutes")
    
    