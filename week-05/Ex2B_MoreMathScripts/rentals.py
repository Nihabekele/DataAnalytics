import math

people = 38
van_capacity = 15
daily_cost = 250

# Calculate number of vans 

num_vans = math.ceil(people / van_capacity)

# Calculate costs
total_cost = num_vans * daily_cost
cost_per_person = total_cost / people

print(f"Total People: {people}")
print(f"Vans needed: {num_vans}")
print(f"Total Rental Cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# a) Charge per person -  $19.74
# b) Total collected - $750.12 (19.74 * 38)
# c) Total cost of vans - $750.00
# d) Leftover money exists because the cost was split evenly among 38 people,
#    but we had to pay for 3 full vans even though the last one wasn't full.
#    Rounding the cents up to .74 also created a small 12 cent surplus.
