# 1. Write a Python code that takes 3 numbers from user and print the greatest one on the screen.

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))
c = int(input("Enter third Number : "))

if a > b:
    if a > c:
        print(f"{a} is greatest number.")
    else:
        print(f"{c} is greatest number.")
else:
    if b > c:
        print(f"{b} is greatest number.")
    else:
        print(f"{c} is greatest number.")