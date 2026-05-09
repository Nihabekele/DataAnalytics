# Lab 2
# 1. Define the current hour (0-23)

hour = 3  

# 2. Updated logic including the late-night condition
if hour >= 23 or hour < 4:
    # This checks 11pm (23) to 3:59am (before 4)
    print("What are you doing up so late??")
elif hour < 10:
    # This checks 4am to 9:59am
    print("Good morning!")
elif hour < 17:
    # This checks 10am to 4:59pm (17:00)
    print("Good day!")
else:
    # This covers 5:00pm (17:00) until 10:59pm (before 23)
    print("Good evening!")
