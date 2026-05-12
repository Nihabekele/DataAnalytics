# Lab 2
# 2
def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")
    print("-" * 20) 

# 3
def add_numbers(*args):
     total = sum(args)
     calculation_string = " + ".join(map(str, args))
     print(f"{calculation_string} = {total}")

# 4
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")
    
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")
    print("-" * 20)

# 5
    # a) Call mailing label twice
display_mailing_label("sara smith", "123 Python Lane", "Boston", "MA", "02108")
display_mailing_label("John Doe", "456 Coding Ave", "Seattle", "WA", "98101")

# b) Call add_numbers three times
add_numbers(10)               # One number
add_numbers(5, 15)            # Two numbers
add_numbers(1, 2, 3, 4, 5)    # Many numbers

# c) Call display_receipt three times
display_receipt(50, 60)       # Overpaid
display_receipt(50, 50)       # Paid exactly
display_receipt(50, 30)       # Underpaid