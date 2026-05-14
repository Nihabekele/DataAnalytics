# Lab 1
# 2. Make a class called Restaurant
class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, rest_name, food_type):
        """Initialize name and food type attributes."""
        self.rest_name = rest_name
        self.food_type = food_type

    # 3a. Add describe_rest() method
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    # 3b. Add rest_open() method
    def rest_open(self):
        print(f"{self.rest_name} is open.")

# 4. Create three instances (objects)
restaurant1 = Restaurant("Weedy's", "Burgers")
restaurant2 = Restaurant("Taco Baco", "Tacos")
restaurant3 = Restaurant("Donkin' Dunnts", "Donuts")

# 5. Call both methods for each instance
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()
