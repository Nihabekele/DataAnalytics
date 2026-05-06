import math 

# I use my birthday day as the diameter 

diameter = 21
radius = diameter / 2

# Formula: Area = Pi * radius * radius

area = math.pi * (radius ** 2)

print("The area of a circle with radius " + str(radius) + " is " + format(area, ".2f"))
