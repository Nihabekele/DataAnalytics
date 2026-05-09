# 2. Set the department code to test

dept_code = 12

# Use match/case
match dept_code:
    case 1:
        dept_name = "Marketing"
    case 5:
        dept_name = "Human Resources"
    case 10:
        dept_name = "Accounting"
    case 12:
        dept_name = "Legal"
    case 18:
        dept_name = "IT"
    case 20:
        dept_name = "Customer Relations"
    case _:
        # The underscore _ is like the else
        dept_name = "Error: Invalid Department Code"

# Print the result
print(f"Department: {dept_name}")

