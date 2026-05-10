# BOnus GAME TIME
# 1. Generate a random number between 1 and 10

# 1. Setup collections (List & Tuple)
number_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# manually mixed these to avoid the 'random' module
shuffled_order = (3, 8, 1, 10, 2, 7, 4, 9, 6, 5)
target_number = shuffled_order[-1] 

# Tracking variables
guess_count = 0
all_guesses = []

print("I'm thinking of a number between 1 and 10.")
guess = 0

while guess != target_number:
    user_input = input("\nEnter your guess: ")

    # FIRST check if it's a number
    if user_input.isdigit():

        guess = int(user_input)
        
        guess_count += 1
        all_guesses.append(guess)

        # Higher or Lower hints
        if guess < target_number:
            print("Higher!")
        elif guess > target_number:
            print("Lower!")
        else:
            print(f"Correct! The number was {target_number}.")
            
            print(f"Game Over! It took you {guess_count} guesses.")
            print(f"Your guesses were: {all_guesses}")
            
            if guess_count < 5:
                print("Wow, you're awesome!")
    
    # If it's NOT a number
    else:
        print("Invalid input! That's not a number. Please try again.")
