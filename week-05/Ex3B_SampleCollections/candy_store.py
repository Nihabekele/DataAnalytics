# Lab 2
#2. A tuple of candy types 
candy_types = ("Gummy Bears", "Skittles", "Lollipops")

# A tuple of fruity flavors
fruity_flavors = ("Mango-Chili", "Blue Raspberry", "Passionfruit")

print(candy_types)
print(fruity_flavors)

# 3. Create the set and add combinations using indexes

candy_combinations = {
    candy_types[0] + " - " + fruity_flavors[1],
    candy_types[1] + " - " + fruity_flavors[0],
    candy_types[2] + " - " + fruity_flavors[2]
}

print(candy_combinations)

# 4. Print the descriptive message and the set

print("Today’s candy options include:")
print(candy_combinations)
