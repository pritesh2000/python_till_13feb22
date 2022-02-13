# Functions
# We put paranthesis after function name only when we want to call it or we are defining it.
"""
def avg(a, b):
    # ans = (a + b)/2
    # return ans
    return (a + b)/2

print("Enter two numbers: ")
x = float(input())  # 5
y = float(input())  # 10
print(f"average of {x} and {y} is: {avg(x, y)}")
"""
"""
def factorial(n):   # n = 5
    f = 1
    i = 1
    while i <= n:   # i = 1,2,3,4,5
        f = f * i   # f = 1 * 2 * 3 * 4 * 5
        i += 1
    return f

print("Enter 5 integers:")
myList = []
for i in range(5):
    myList.append(int(input()))
factorials = []
for n in myList:
    factorials.append(factorial(n))
for ans in factorials:
    print(ans)
"""
# Perfect numbers between two given integers
"""
def perfectCheck(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False

print("Enter two integers:")
a = int(input())
b = int(input())
for m in range(a, b+1):
    if perfectCheck(m) == True:
        print(m)
"""
# Lambda Functions
"""
print("Enter two integers:")
a = int(input())
b = int(input())
sqrt = lambda n : n ** 0.5
ans = sqrt(a) + sqrt(b)
print(ans)

armCheck = lambda n : True if sum([int(char)**len(str(n)) for char in str(n)]) == n else False
print(armCheck(a))
print(armCheck(b))
"""

# Docstrings:
'''
import random
def avg(a,b,c,d,e):
    """Returns average of 5 numbers"""
    return (a+b+c+d+e)/5

print(avg.__doc__)
random.randint(1, 100)
'''
# Passing functions into another functions as arguments
'''
def fact(n):   # n = 5
    f = 1
    i = 1
    while i <= n:   # i = 1,2,3,4,5
        f = f * i   # f = 1 * 2 * 3 * 4 * 5
        i += 1
    return f

def avg(a,b,c,d,e):
    """Returns average of 5 numbers"""
    return (a+b+c+d+e)/5

print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(f"The average of factorials of {a}, {b}, {c}, {d} & {e} is:", avg(fact(a), fact(b), fact(c), fact(d), fact(e)))
'''
'''
def average_of_factorial(a, b, c):
    def fact(n):
        f = 1
        for x in range(1, n+1):
            f *= x
        return f
    return (fact(a)+fact(b)+fact(c))/3

average_of_factorial(5,6,7)
fact(5)
'''
# scope of a function
"""
a = 10                      # global variable

def func1():
    def func2():
        print(d)
    global b
    a = 50
    a += 1
    print(a)
    b += 1
    print(b)
    # print(c)              Error
    d = 40                  # local variable of func1()
    func2()
    func3()

def func3():
    # print(d)
    pass

b = 20                      # global variable for all the functions called after this point
func1()
c = 30
print(a)
print(b)
"""
# passing collections into function:
"""
def avg(n):
    return sum(n)/len(n)

myList = []
l = int(input("How many numbers do you want to enter? "))
print(f"Enter {l} numbers:")
for i in range(l):
    myList.append(float(input()))
print(myList)
myTuple = tuple(myList)
print(f"Average = {avg(myTuple)}")
"""
# args & kwargs: variable length arguments
"""
def avg(*args):
    # print(args)
    return sum(args)/len(args)

def percent(**kwargs):
    # print(kwargs)
    return sum(kwargs.values())/len(kwargs)

print("Average =", avg(15, 20, 25, 30))

print("Percentage =", percent(Physics = 85, Maths = 92, Computers = 98))     # kwargs
"""
# functions with positional arguments, **args and **kwargs
"""
def func1(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

# func1(1,2,3)
func1(1,2,3,4,5,6,7,8,9,10,11,12, name = "Sunder", age=21, country="India")
"""

# default arguments
"""
def func1(a, b=10, c=20):
    print(a)
    print(b)
    print(c)

# func1(5)
# func1(5, 15)
func1(5, 15, 25)
"""
# Recursive Functions
# 5! = 5*4*3*2*1    =>  5! = 5 * 4!
"""
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1 * 0!
0! = 1

Recursive step:
n! = n * (n-1)!
basis step:
if n == 0:
factorial = 1
"""


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(7))





"""
HW:
0.Write a Python code to create a 3x3 matrix using nested lists, with values given by user. Also print it in a way that it looks like a matrix.
Next, upgrade your program for the dimension n x n where n is given by user.

1.Make a Python program that uses a function to find average of 3 given numbers and print it on the screen.

2.Make a Python program that uses a function that finds factorial of the number given in its argument.

3.Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.

4.Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.

5.Make a Python program that asks 5 numbers from user, finds their factorials using a function that takes 1 number in its argument & returns its factorial, adds all the factorials returned by function & prints the final answer on the screen.

6.Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()

7. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

# Recursion
8. Write a Python code to print nth term of an AP whose first term 'a' & common difference 'd' are given.
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

9. Make a Python program that finds nth term of a Geometric Progression whose first term (a)
and common ratio (r) are given by user. Find out more about Geometric Progression from internet.

10. Make a recursive Python function that returns nth term of fibonacci sequence. Develop a Python main program around this function that asks term number from the user and prints that term of fibonacci sequence on the screen.
Fibonacci sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21.......

11. Write a function to calculate power of a number raised to other ( a^b ) using recursion.

12. Make a Python program that uses recursion to print multiplicative table of 12.

"""