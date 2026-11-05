rate = 7.1

monthly_installment = float(input("Enter monthly installment: "))
months = int(input("Enter duration in months: "))

if monthly_installment < 500:
    print("Invalid input: Monthly installment must be at least Rs. 500")

elif months < 6:
    print("Invalid input: Duration must be at least 6 months")

else:
    principal = monthly_installment * months
    time = months / 12
    interest = (principal * rate * time)/100

    maturity_amount = principal+interest

    print("Total deposited amount:", principal)
    print("Interest earned:", interest)
    print("Maturity amount:", maturity_amount)