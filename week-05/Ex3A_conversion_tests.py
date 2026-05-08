# Lab 1
#  Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

# 2. Define the following variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '


# 3. Perform transformations and create a new variable for each.

# Testing variable a
# a_int = int(a)      # ERROR ValueError (decimal string to int)
a_float = float(a)    # Success
a_complex = int(float(a))

# Testing variable b
b_int = int(b)        # Success
b_float = float(b)    # Success

# Testing variable c
# c_int = int(c)      # ERROR ValueError (contains letters)
# c_float = float(c)  # ERROR ValueError (contains letters)

# Testing variable d
# d_int = int(d)      # ERROR  ValueError (contains letters)
# d_float = float(d)  # ERROR  ValueError (contains letters)


# 4. Print the value of each variable and its type

# Original Variables
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# New Transformed Variables 
print(a_float, type(a_float))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(a_complex, type(a_complex))

# 5a. int(a) valueError because it has a decimal point ,int(b) worked because it's a clean number. 
# int(c) and int(d) ValueError because they contain letters.

# 5b. float(a) and float(b) worked. 
# float(c) and float(d) ValueError because of letters.

# 5c. For variable a, I used int(float(a)) to strip the decimal first.
# This worked and gave me the integer 101.

# 5d. Use slicing to get numeric portions and cast to integer
c_slice = c[0:3]           
c_numeric = int(c_slice)   # Success

d_slice = d[7]             
d_numeric = int(d_slice)   # Success

# 5e. Use .strip() inside a print statement

print(f"Variable a stripped: '{a.strip()}'")
print(f"Variable d stripped: '{d.strip()}'")

# Final check for the sliced variables
print(c_numeric, type(c_numeric))
print(d_numeric, type(d_numeric))
