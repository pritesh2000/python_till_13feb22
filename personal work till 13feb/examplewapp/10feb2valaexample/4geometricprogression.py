# 4.Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.

a = int(input("Enter first term : "))
r = int(input("Enter difference : "))

n = int(input("Enter nth term of geometric progression : "))

def geo_prog(a, r, n):
    """
    This is used for finding Nth term's value of Geometric Progression.
    where 'a' is first term and 'r' is common ratio between two terms.
    """
    if n==1:
        return a 
    else:
        return r * geo_prog(a, r, n-1)

print(geo_prog(a, r, n))
