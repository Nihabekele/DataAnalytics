# Exercise 2.A Make calculations with Python
# Lab 1

# Formula: Total Due is determined by: Food Cost + Tax + Tip

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# a. Answer about str()
# The str() function converts a number into a string (text). 
# This is needed because Python cannot add text and numbers together in one print statement.

# Display the results
#print("The total due is " + str(total_due)) # I will comment this out in question 5

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Total due is " + str(total_due))

print("Tip is " + format(tip, ".2f"))
