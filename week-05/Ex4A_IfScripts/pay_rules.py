# Lab 2
# 1. Define the variables 
pay_rate = 25.00
hours_worked = 45

# Check for overtime using an if/else 
if hours_worked > 40:
    # Calculate regular pay for the first 40 hours
    regular_pay = 40 * pay_rate
    
    # Calculate the extra hours and the higher rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    
    # Total gross pay
    gross_pay = regular_pay + overtime_pay
    print("Overtime worked")
else:
    # No overtime simple calculation 
    gross_pay = hours_worked * pay_rate
    print("No overtime worked.")

#  Print the final result
print(f"Total Gross Pay: ${gross_pay}")

# 3.Run your script several times with different values for pay_rate and hours_worked
# and confirm the output is right.

# Define the variables for testing

pay_rate = 25.50
hours_worked = 40

# Check for overtime using an if/else block
if hours_worked > 40:
    # Calculate regular pay for the first 40 hours
    regular_pay = 40 * pay_rate
    
    # Calculate the extra hours (anything over 40)
    overtime_hours = hours_worked - 40
    
    # Calculate overtime at 1.5x the rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    
    # Add them together for the gross pay
    gross_pay = regular_pay + overtime_pay
    print("Overtime worked!")
else:
    # If hours are 40 or less, use simple multiplication
    gross_pay = hours_worked * pay_rate
    print("No overtime worked.")

#  Print the final result formatted to two decimal places
print(f"Total Gross Pay: ${gross_pay:.2f}")
