# lab 3
# 1. Define the dictionary

contact_info = {
    "name": "Maria Mayo",
    "address": "123 Potomac Ave",
    "city": "Alexandria",
    "state": "VA",
    "zip": "22301"
}

# 2. Print using a multi-line f-string

print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

# 3. Remove the 'name' key

del contact_info["name"]

# 4. Create the full_name dictionary

full_name = {
    "first name": "Maria",
    "last name": "Mayo"
}

# Assign it to the contact_info dictionary under a new key

contact_info["full_name"] = full_name

print(contact_info)

# 5. Use .update() to add the honorific to the nested full_name dictionary

contact_info["full_name"].update({"honorific": "Ms."})

# Print the whole dictionary to see the update

print(contact_info)

# 6. Using .update() to add the full_name dictionary to contact_info

contact_info.update({"full_name": full_name})

# 7. Print the formatted address with the new nested items

print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

