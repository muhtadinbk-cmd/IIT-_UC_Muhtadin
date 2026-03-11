income = float(input("What is your income"))

if income <= 20000:
    tax = income * 0.02
elif income <= 50000:
    tax = 400 + 0.025 * (income - 20000)
else :
    tax= 1150 + .035 *(income - 50000)

print("Your tax is ", tax)
