# Lab 3

# 1. Create a list of skills
my_skills = ["Python", "Data Analysis", "Machine Learning", "SQL", "Data Visualization"]

print(my_skills)

# 2. Using enumerate() to create a numbered list
for index, skill in enumerate(my_skills, start=1):
    print(f"{index}. {skill}")


# 3. Use enumerate with an if statement

for count, skill in enumerate(my_skills, start=1):
    # Check if it's the first item
    if count == 1:
        print(f"{count}. {skill} <- top pick!")
    else:
        print(f"{count}. {skill}")


 # 4. Reverse the list but keep the numbering 1-5
 
for count, skill in enumerate(reversed(my_skills), start=1):
    if count == 1:
        print(f"{count}. {skill} <- top pick!")
    else:
        print(f"{count}. {skill}")
