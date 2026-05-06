# Define values
# bill = 48.00
# tip_percent = 15 # This means 15%

# Calculate tip (percent divided by 100)
# tip = bill * (tip_percent / 100)

# I use format with .2f to show it as money

# print("The tip on a $" + format(bill, ".2f") + " restaurant bill is $" + format(tip, ".2f"))


# Modifying tip_amount.py to use input()

# PITFALL input() always returns a string (text). 
# I use float() so the user can type decimals

bill = float(input("How much was your restaurant bill? "))
tip_percent = float(input("What percentage would you like to tip? "))

tip = bill * (tip_percent / 100)

print("The tip on a $" + format(bill, ".2f") + " restaurant bill is $" + format(tip, ".2f"))

# My Observations 
# 1. Pitfall - If the user types a letter or a '$', the program gets ValueError.
# 2. Pitfall - If I forget to use float(), Python gives an error because I can't multiply text.
# 3. Pitfall - If the user leaves the input blank, the program gets ValueError it cannot be converted to a float.
