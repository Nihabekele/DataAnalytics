# Define values

savings = 5000.00
interest_rate_decimal = 0.08  # 8% as a decimal
interest_rate_whole = 8      # 8% as a whole number for the rule

years_to_double = 72 / interest_rate_whole
doubled_savings = savings * 2

# results
print("Your current savings is " + str(savings))

# I Use .0% for the interest rate and .2f for the money
# I Use .1f for the years as requested

print("At a " + format(interest_rate_decimal, ".0%") + " interest rate, your savings account will be")
print("worth " + format(doubled_savings, ".2f") + " in " + format(years_to_double, ".1f") + " years")
