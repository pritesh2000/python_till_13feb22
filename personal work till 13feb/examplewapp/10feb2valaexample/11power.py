"""
11. Write a function to calculate power of a number raised to other ( a^b ) using recursion.
"""

def power(a, b):
    """This function gives you value of 'a^b' """
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)
 
x = int(input("Enter base : "))
y = int(input("Enter power : "))
print(power(x, y))

