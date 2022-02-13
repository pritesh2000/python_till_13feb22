"""
8. Write a Python code to print nth term of an AP whose first term 'a' & common difference 'd' are given.
        ------------------repeated---------------   
        explaination:
        first term = a = 6
        common diff = d= 4
        6, 10, 14, 18, 22, 26, 30, 34
        8th term = 7th term + d
        nth term = (n-1)th term + d
        a = 7
        d = 14
        5th term = ?
        2nd term = 1st term + d
        1st term = a
"""
from random import randint

a = int(input("Enter first term of AP : "))
d = int(input("Enter common difference in AP : ")) 
n = randint(1,10)
def arth_prog(n):
    print(f"{n}th term of AP is : ")
    return a + (n-1)*d
print(arth_prog(n))