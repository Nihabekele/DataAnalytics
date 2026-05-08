# bonus
# 1. Set the year 
year = 2024

# Apply the Gregorian rules
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

# Print the result
if is_leap:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is NOT a leap year.")

# 3. Run it several times with different values for the year. Make sure to test the years
#1900, 1950, 1999, 2000, 2001, and 20212.

year = 2001

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is NOT a leap year.")

    