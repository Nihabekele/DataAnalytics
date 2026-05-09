# Lab 4
# 1. Assign values to variables a, b, and c
a = 27
b = 21
c = 12

# Finding the Smallest 
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Finding the Largest 
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# results
print(f"The numbers are: a={a}, b={b}, c={c}")
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
