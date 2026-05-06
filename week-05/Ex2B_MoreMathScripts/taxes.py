# withheld for taxes
salary = 4500.00
tax_rate = 0.23
tax_withheld = salary * tax_rate

# I use the format function 
formatted_tax = format(tax_withheld, ".2f")

print("Monthly Salary: $" + format(salary, ".2f"))
print("Tax Withheld: $" + formatted_tax)