"""
Author : Pritesh Tadvi
Date : 12-02-2022
Topic : Various formulas' combination
"""


def avg(a, b, c):
    """This function is use to find average of 3 numbers."""
    return (a+b+c)/3


def fact(n):
    """This function is used for Calculate factorial of a specific number."""
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def arth_prog(a, d, n):
    """Used for finding Nth term's value of Arithmetic Progression.
    where   'a' is first term and 'd' is common difference between two terms. """
    if n == 1 :                             
        return a                            
    else:                                   
        return d + arth_prog(a, d, n-1)

def geo_prog(a, r, n):
    """
    This is used for finding Nth term's value of Geometric Progression.
    where 'a' is first term and 'r' is common ratio between two terms.
    """
    if n==1:
        return a 
    else:
        return r * geo_prog(a, r, n-1)

def fibo(n):
    """This function returns value of Fibonacci number of given number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def power_ab(a, b):
    """This function gives you value of 'a^b' """
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power_ab(a, b-1)

if __name__ == "__main__":
    print("This is formulas.")
