# Lab 1
# 1. ValueError
# Turning text into an integer

try:
    my_number = int("abc") 
except ValueError:
    print("ValueError: You can't turn text into a number if it doesn't look like a digit!")
else:
    print(f"Success! Your number is: {my_number}")
finally:
    print("Let's try another one...")


    # 2. NameError
# I never created 'banana', so Python won't recognize it

try:
     print(banana) 
except NameError:
    print("NameError: You are calling a variable that hasn't been created yet!")
else:
    print("Variable found!")
finally:
     print("Let's try another one...")

    # 3. TypeError
   #  Adding a string and an integer

try:
    result = 10 + "ten"
except TypeError:
    print("TypeError: You can't perform math on different types like strings and numbers!")
else:
    print(f"The result is {result}")
finally:
    print("Let's try another one...") 


    # 4. SyntaxError
    # Missing a closing parenthesis

try:
    eval('print("Hello"') 
except SyntaxError:
    print("SyntaxError: There is a typo in the way the code is written like a missing bracket")
else:
    print("Perfect syntax!")
finally:
    print("Let's try another one...")
