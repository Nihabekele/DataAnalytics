import math

# Room dimensions
length = 20
width = 15
tiles_per_box = 12

# 1. Calculate area and add 10% extra

area = length * width
total_tiles_needed = area * 1.10  # 1.10 adds the 10% automatically

# 2. Calculate boxes (Total tiles / 12)
# I use math.ceil because I can't buy partial boxes

boxes_needed = math.ceil(total_tiles_needed / tiles_per_box)

print(f"Room Area: {area} sq ft")
print(f"Tiles needed (with 10% extra): {total_tiles_needed:.2f}")
print(f"Total boxes to buy: {boxes_needed}")
