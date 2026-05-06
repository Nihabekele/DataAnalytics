# calculate the distance between coordinates 
import math

# Coordinates (x1, y1) and (x2, y2)
x1, y1 = 1, 2
x2, y2 = 4, 6

# Calculate the difference and square it
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")
