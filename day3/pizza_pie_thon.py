print("Welcome to Python Pizza Deliveries!")

# GLOBAL VARIABLES
size = input("What size pizza do you want? s, m or l: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")
pizza_price = 0.00

# todo: work out how much they need to pay based on their size choice
if size == 's':
    pizza_price += 15.00
    if pepperoni == "y":
        pizza_price +=2.00
        print(f"if OUTPUT {pepperoni} { pizza_price} -loc:14 debugging")
        if extra_cheese == 'y':
            pizza_price += 1.00
elif size == 'm':
    pizza_price = 20.00
    if pepperoni == "y":
        pizza_price +=3.00
        print(f"elif_1 OUTPUT {pepperoni} {pizza_price} -loc:21 debugging")
        if extra_cheese == 'y':
            pizza_price += 1.00
elif size == 'l':
    pizza_price = 25.00
    if pepperoni == "y":
        pizza_price +=3.00
        print(f"elif_2 OUTPUT {pepperoni} {pizza_price} -loc:28 debugging")
        if extra_cheese == 'y':
            pizza_price += 1.00

print(f"Your Final bill is ${pizza_price} Thank you!")


#------------------------------------------------------
#               MUCH DRYER VERSION
#------------------------------------------------------
'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")



'''