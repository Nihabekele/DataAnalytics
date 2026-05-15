# Lab 1
#  Make a class called Restaurant
class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, rest_name, food_type):
        """Initialize name and food type attributes."""
        self.rest_name = rest_name
        self.food_type = food_type

#  Add a default attribute
        self.number_served = 0
        self.customer_ratings = []

    #  Add describe_rest() method
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

#  Add add_num_served() method
    def add_num_served(self):
        amount = int(input(f"How many customers served today at {self.rest_name}? "))
        self.number_served += amount

    #  Add print_num_served() method
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    #  Add customer_rating() method
    def customer_rating(self):
        while True:
            # I use input as a string first to check it
            rating_input = input("How would you rate your experience (1-5)? ")
            
            # Check if it is a number AND if it's between 1 and 5
            if rating_input.isdigit() and 1 <= int(rating_input) <= 5:
                rating = int(rating_input)
                self.customer_ratings.append(rating)
                break  # Stop the loop and move to the math
            else:
                # If they type "6" or "abc", show this message:
                print("Invalid input. Please enter a whole number between 1 and 5.")
        
        # Calculate the average after getting a valid number
        avg = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The average rating for this restaurant is {avg:.1f}")

    #  Add rest_open() method
    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Create three instances (objects)
restaurant1 = Restaurant("Weedy's", "Burgers")
restaurant2 = Restaurant("Taco Baco", "Tacos")
restaurant3 = Restaurant("Donkin' Dunnts", "Donuts")

# Call both methods for each instance
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

#  Test new methods for restaurant1
print("--- Testing Restaurant 1 ---")
restaurant1.print_num_served()

# Run add_num_served a few times
restaurant1.add_num_served()
restaurant1.add_num_served()

# Check updated balance
restaurant1.print_num_served()

# Test the rating system
print("\n--- Testing Ratings ---")
restaurant1.customer_rating()
restaurant1.customer_rating()
