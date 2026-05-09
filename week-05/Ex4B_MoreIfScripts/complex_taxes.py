# Lab 3
# 1. Copy of pay_rules.py logic 
pay_rate = 17.30
hours_worked = 45

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    weekly_gross_pay = regular_pay + overtime_pay
else:
    weekly_gross_pay = hours_worked * pay_rate

# 2. Calculate Annual Gross Pay 
# I assume 52 weeks in a year
annual_gross_pay = weekly_gross_pay * 52

# Print the results so far
print(f"Weekly Gross Pay: ${weekly_gross_pay:.2f}")
print(f"Annual Gross Pay: ${annual_gross_pay:.2f}")

# 3. Use a series of if statements to determine the appropriate tax rate.
# Calculate Weekly Pay 
pay_rate = 17.30
hours_worked = 45

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
    weekly_gross = regular_pay + overtime_pay
else:
    weekly_gross = hours_worked * pay_rate

#  Annual Income 
annual_income = weekly_gross * 52
status = 'single' # I can Change here to 'joint' to test the other table

#  Tax Logic 
tax_rate = 0

if status == 'single':
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
        
elif status == 'joint':
    if annual_income < 12000:
        tax_rate = 0.00
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

#  Final Calculations 
tax_amount = annual_income * tax_rate
net_income = annual_income - tax_amount

print(f"Annual Income: ${annual_income:,.2f}")
print(f"Status: {status}")
print(f"Tax Rate: {tax_rate * 100}%")
print(f"Tax Owed: ${tax_amount:,.2f}")


# 4. Weekly Tax Withholding 

weekly_tax_withheld = weekly_gross * tax_rate
weekly_net_pay = weekly_gross - weekly_tax_withheld

print(f"Weekly Tax Withheld: ${weekly_tax_withheld:.2f}")
print(f"Weekly Net Pay (Take-home): ${weekly_net_pay:.2f}")


# 5. Formatted Output 

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross:.2f}")
print(f"Your filing status is {status}")
print(f"Your tax withholding for the week is ${weekly_tax_withheld:.2f}")
print(f"Your net pay is ${weekly_net_pay:.2f}")
