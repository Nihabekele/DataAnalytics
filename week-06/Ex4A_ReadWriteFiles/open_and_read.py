# 10 a. Open the file in read mode ('r')
# f = open("about_me.txt", "r")

#  10b. Print the contents using .read()
# print("--- Full File Content ---")
# print(f.read())

# # 10c. Close the file
# f.close()

#  Question 12
# f = open("about_me.txt", "r")

#  Read the first 50 characters
# print("First 50 characters:")
# print(f.read(50))

#  Read the next 50 characters
# print("\nNext 50 characters:")
# print(f.read(50))

# f.close()

# f = open("about_me.txt", "r")

# 13a. Read a specific number of characters in a line, then the rest
# print("Readline(10):", f.readline(10))
# print("Rest of the line:", f.readline())

# # 13b. I Use a loop to read the next 4 lines
# print("\n--- Reading with a Loop ---")
# for i in range(1, 5):
#     print(f.readline())

# f.close()

# Open the file again for Question 14
# f = open("about_me.txt", "r")

# 14a & b. Try readlines() with no argument
# print("--- Readlines Output ---")
# print(f.readlines()) 

# f.close()

#f = open("about_me.txt", "r")
# 14c & d. Testing .readlines(10) 
# print("--- Readlines(10) ---")
# print(f.readlines(10)) 

# 14e. Testing .readlines(100) and .readlines(-1)
# print("\n--- Readlines(100) ---")
# print(f.readlines(100))

# Resetting the file 
# f.seek(0) 
# print("\n--- Readlines(-1) ---")
# print(f.readlines(-1))

# f.close()

# Open the file one last time
f = open("about_me.txt", "r")

# 15a. Variable using .read(50)
first_part = f.read(50)

# 15b. Capture the next 4 lines into a list using a loop
# (I use .strip() to clean up the extra spacing)
next_four = []
for i in range(4):
    line = f.readline().strip()
    if line: 
        next_four.append(line)

# 15c. Variable using .readlines(100)
remaining_part = f.readlines(100)

f.close()

# 16. The Final Print Output
print(f"First 50 characters: {first_part}")
print(f"Next four lines, as list by line: {next_four}")
print(f"Next 100 characters, as list by line: {remaining_part}")
