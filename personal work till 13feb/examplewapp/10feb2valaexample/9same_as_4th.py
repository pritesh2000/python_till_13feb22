"""
------------------repeated---------------
9. Make a Python program that finds nth term of a Geometric Progression whose first term (a)
and common ratio (r) are given by user. Find out more about Geometric Progression from internet.
"""
from random import randint


a = int(input("Enter first term of GP : "))
r = int(input("Enter common ratio of GP : "))
# n = randint(1,10)
n = int(input("nth : "))
def geo_prog(n):
    print(f"{n}th term of GP is :")
    return a * r**(n-1)

print(geo_prog(n))