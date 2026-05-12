# Lab
# 1.
import random
import math
import statistics

# 2. Starting Variables
vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3, 10)
pi = math.pi

#3. Calculations 

# Calculations for Sample (75 values)
sample_sum = sum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_med = statistics.median(vals_sample)

# Calculations for Superset (200 values)
super_avg = statistics.mean(vals_choices)
super_med = statistics.median(vals_choices)
super_mode = statistics.mode(vals_choices)
super_std = statistics.stdev(vals_choices)
super_var = statistics.variance(vals_choices)

# Circle Calculations
# Area formula: pi * r squared
raw_area = pi * (radius ** 2)
area_up = math.ceil(raw_area)
area_down = math.floor(raw_area)


print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_avg}")
print(f"Median of 75 sample values: {sample_med}")

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {super_avg}")
print(f"Median of 200 values: {super_med}")
print(f"Mode of 200 values: {super_mode}")
print(f"Standard deviation of 200 values: {super_std}")
print(f"Variance of 200 values: {super_var}")

print('\n')

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_down} (rounded down to the nearest integer)")