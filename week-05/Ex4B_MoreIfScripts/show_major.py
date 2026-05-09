# Lab
# 1. Define variables
student_name = "Liya"
student_major = "MKT"  # I can try changing this to test different codes

# Lookup Logic
if student_major == "BIOL":
    major_name = "Biology"
    location = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    location = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    location = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    location = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    location = "Westly Hall, Room 310"
else:
    # Handle codes not in the table
    major_name = "<unknown>"
    location = ""

# result 
print(f"Student: {student_name}")
print(f"Major: {major_name}")
if location:    # Only prints location if it's not empty
    print(f"Office: {location}")
