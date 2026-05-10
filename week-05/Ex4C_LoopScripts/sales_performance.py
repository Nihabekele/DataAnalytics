# Lab 4
# 1.list of sales records
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]


# 2. Use a for loop to unpack the three items in each tuple

for name, region, sales in sales_data:

    # using an f-string with money formatting

    print(f"{name} ({region}): ${sales:,.2f}")


# 3. Loop through the data and unpack the tuple
for name, region, sales in sales_data:
    # Print the main summary line first
    print(f"{name} ({region}): ${sales:,.2f}")
    
    # Check if they sold more than $5000
    
    if sales > 5000:
        print(" ^ Top performer!")


# 4 B0nus

# Create a variable to track total sales 
grand_total = 0

# existing loop
for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")
    
    # Add the current person's sales to the grand_total
    grand_total += sales
    
    if sales > 5000:
        print(" ^ Top performer!")

# Print the final total after the loop finishes 
print(f"Overall Total Sales: ${grand_total:,.2f}")
    
    