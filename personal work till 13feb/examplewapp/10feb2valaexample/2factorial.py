# 2.Make a Python program that uses a function that finds factorial of the number given in its argument.
"""
num = int(input("Enter number : "))
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1

print("Factorial of",num, "is", fact)
"""

# recursive function

def fact(n):
    """This function is used for Calculate factorial of a specific number."""
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(6))
