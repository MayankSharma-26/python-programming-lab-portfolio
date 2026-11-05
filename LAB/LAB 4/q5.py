k = int(input("Enter Kilometers: "))
period = int(input("Press 1 For Day,\nPress 2 For Night: "))
if period == 1:
    taxi = 33.58 + 37.89 * k
    if k >= 20:
        Bus = 4.32 * k

    if k >= 100:
        Train = 2.88 * k

    if k < 20:
        print("Taxi is the cheapest mode of transport with", taxi, "INR")

    elif k < 100:
        if taxi < Bus:
            print("Taxi is the cheapest mode of transport with", taxi, "INR")
        else:
            print("Bus is the cheapest mode of transport with", Bus, "INR")

    else:
        cheapest = min(taxi, Bus, Train)

        if cheapest == taxi:
            print("Taxi is the cheapest mode of transport with", taxi, "INR")
        elif cheapest == Bus:
            print("Bus is the cheapest mode of transport with", Bus, "INR")
        else:
            print("Train is the cheapest mode of transport with", Train, "INR")
elif period == 2:
    taxi = 33.58 + 43.17 * k

    if k >= 20:
        Bus = 4.32 * k

    if k >= 100:
        Train = 2.88 * k
    if k < 20:
        print("Taxi is the cheapest mode of transport with", taxi, "INR")
    elif k < 100:
        if taxi < Bus:
            print("Taxi is the cheapest mode of transport with", taxi, "INR")
        else:
            print("Bus is the cheapest mode of transport with", Bus, "INR")
    else:
        cheapest = min(taxi, Bus, Train)

        if cheapest == taxi:
            print("Taxi is the cheapest mode of transport with", taxi, "INR")
        elif cheapest == Bus:
            print("Bus is the cheapest mode of transport with", Bus, "INR")
        else:
            print("Train is the cheapest mode of transport with", Train, "INR")

else:
    print("Invalid period")
    
    