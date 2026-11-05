w= float(input("Enter weight in kg"))
h= float(input("Enter height in m"))
bmi= w/(h**2)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<24.9:
    print("Normal weight")
elif bmi>=25 and bmi<29.9:
    print("Overweight")
elif bmi>=30:
        print("Obesity")