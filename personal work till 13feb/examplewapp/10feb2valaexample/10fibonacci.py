"""
10. Make a recursive Python function that returns nth term of fibonacci sequence. Develop a Python main program around this function that asks term number from the user and prints that term of fibonacci sequence on the screen.
Fibonacci sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21.......
"""
from ntpath import join


num = int(input("For which number till you want fibonacci series : "))
def fibonacci(n):
    """This function returns value of Fibonacci number of given number"""
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci sequence is: ")
 

for i in range(num):
    print(fibonacci(i),end=", ")
print(join("......"))



