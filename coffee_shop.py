#Step 1
print("Welcome to the Python Coffee Shop")

#Take input
print("Welcome to the Python Coffee Shop!")

price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50

customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")

order_again = "yes"

while order_again == "yes":

    print("\nMenu")
    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Mocha: $" + str(price_mocha))

    choice = input("What would you like to order? (coffee/latte/mocha): ")

    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_mocha
    else:
        print("Sorry, we do not have that.")
        cost = 0

    quantity = int(input("How many cups would you like? "))
    total_cost = cost * quantity

    if quantity > 1:
        print("You get a discount of $1.00!")
        total_cost -= 1.00

    student = input("Are you a student? (yes/no): ")

    if student == "yes":
        print("Student discount applied (10%)!")
        total_cost = total_cost * 0.9

    print("Your total is: $" + str(round(total_cost, 2)))

    order_again = input("Would you like to place another order? (yes/no): ").lower()

print("Thank you, " + customer_name + "! Please come again.")
