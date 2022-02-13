# 3. A shop gives discount of 10% if the cost of purchased quantity is more than Rs.1000.
# Ask user for quantity
# Assume each item costs 100.
# Calculate and print total amount to be paid by user.



qty = int(input("Enter items you want to purchase: "))


if qty >= 10:
    price = (qty * 100)/10
    print(f"You will got discount of 10% which is {price}") 
else:
    print("Thank you for purchase next buy more to get discount.")
