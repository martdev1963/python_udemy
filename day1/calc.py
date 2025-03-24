
# greeting
print("Welcome to the tip calculator!")

# user input
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# calculations
# tip as percent
tp = tip / 100 # convert from int to float...
#alt calculation:
#bill_with_tip = bill * (1 + tip / 100)
#print(bill_with_tip)
tip_amount = bill * tp
total = bill + tip_amount
split = total / people
#round(split, 2)


# output
print(tp)
print(tip_amount)
print(people)
print(total)
print(people)
print(f"Each person should pay: ${round(split, 2)}")


# tip formula
# 12% = 12 / 100  = 0.12
# 150 * 1.12 / 5