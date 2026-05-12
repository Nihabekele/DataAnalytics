# Lab 1 
# Question 2
import random

# Question 3
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',   'Headset', 'Docking Station', 'USB Hub',
 'Desk Lamp', 'Surge Protector']

# Question 4a
product_of_day = random.choice(products)
print(f"Product of the Day: {product_of_day}")
# b
survey_items = random.sample(products, 3)
print(f"Survey Products: {survey_items}")
# c
random.shuffle(products) # This shuffles the list "in place"
print(f"Shuffled Inventory: {products}")
# d
transactions = random.randint(50, 300)
print(f"Daily Transaction Count: {transactions}")
