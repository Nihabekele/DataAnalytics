# Define values
bill = 48.00
tip_percent = 15 # This means 15%

# Calculate tip (percent divided by 100)
tip = bill * (tip_percent / 100)

# I use format with .2f to show it as money

print("The tip on a $" + format(bill, ".2f") + " restaurant bill is $" + format(tip, ".2f"))
