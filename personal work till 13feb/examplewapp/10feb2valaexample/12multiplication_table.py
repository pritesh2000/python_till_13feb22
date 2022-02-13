"""
12. Make a Python program that uses recursion to print multiplicative table of 12.
"""

def multiplication_table(n, i):
    if i > 10:
        return
    
    print(f"{n} x {i} = {n*i}")

    return multiplication_table(n, i+1)

n = int(input("Enter number for multiplication table : "))
multiplication_table(n, 1)
        