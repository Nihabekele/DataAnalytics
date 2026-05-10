# Lab 2
# 2. Define variables

bank_balance = 500       # Starting amount
savings_goal = 1200      # What I want to reach
weekly_savings = 150     # How much I save each week
treat_cost = 20

# 3.Use a while loop to check if the goal is met
# Lines 13-19 are commented out so that the program starts with the original $500 
# balance for the new logic in Question 4

# # while bank_balance < savings_goal:
#     # Add the weekly savings to the balance
#     bank_balance = bank_balance + weekly_savings
#     print(f"This week my balance increased to ${bank_balance}")

# # Once the loop exits, it means the goal is met
# print(f"Goal met! My current balance is ${bank_balance}")


# 4. Try adding additional logic to the loop

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings
    
    # a) 75% Check (I have do this first so the treat logic isn't skipped by the 50% rule.)
    if bank_balance >= (savings_goal * 0.75):
        bank_balance = bank_balance - treat_cost
        print(f"So close! After treating myself, my balance is up to ${bank_balance}")
    
    # b) 50% Check (I have do this second)
    elif bank_balance > (savings_goal / 2):
        print(f"Almost there! This week my balance is up to ${bank_balance}")
    
    else:
        print(f"This week my balance increased to ${bank_balance}")

print(f"Goal met! My current balance is ${bank_balance}")
