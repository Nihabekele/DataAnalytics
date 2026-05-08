#Lab 2
# 2. Defining the messy data 
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# 3. Use .lower() to convert all three names to lowercase, and print each result.
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# 4. Use .title() to convert names to title case and print each result
print(name_1.title())
print(name_2.title())
print(name_3.title())

# 5. Use .replace() to remove the $ and print each result
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")

print(salary_1_clean)
print(salary_2_clean)

print(type(salary_1_clean))


# 6. Chain .replace() for $ and int()
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int)
print(type(salary_1_int))
