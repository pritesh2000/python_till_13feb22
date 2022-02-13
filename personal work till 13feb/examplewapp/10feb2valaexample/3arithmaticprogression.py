# 3.Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.

a = int(input("Enter first term : "))
d = int(input("Enter common difference : "))

n = int(input("Enter nth term of arithmetic progression : "))

def arth_prog(a, d, n):
    """Used for finding Nth term's value of Arithmetic Progression.
    where   'a' is first term and 'd' is common difference between two terms.  
    """
    if n == 1 :                             
        return a                            
    else:                                   
        return d + arth_prog(a, d, n-1)

print(arth_prog(a, d, n))

