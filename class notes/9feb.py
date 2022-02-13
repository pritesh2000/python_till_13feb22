# Most frequent use of while loop:
"""
infinite while loop
"""
"""
print("Enter two numbers:")
a = float(input())
b = float(input())
while True:
    choice = input("What do you want to do? +, -, * or /?\nOr\nPress 'Q' to quit\n")
    # There is no switch case in Python
    if choice == "+":
        print(f"{a} + {b} = {a+b}")
    elif choice == "-":
        print(f"{a} - {b} = {a-b}")
    elif choice == "*":
        print(f"{a} * {b} = {a*b}")
    elif choice == "/":
        print(f"{a} / {b} = {a/b}")
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Invalid Operation, Please Try Again...")
"""
# fruits = ["apple", "banana", "kiwi", "mango", "strawberry"]
"""
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
"""
"""
for (i=0; i<5; i++)     # i = 0,1,2,3,4
{

}
"""
# for fruit in fruits:        # i = "apple", "banana", "kiwi", "mango", "strawberry"
#     print(fruit)

# for loop in strings
"""
name = "Python@Royal"
# ind:  012345......
for character in name:      # x = "P", "y", "t".....
    print(character)
"""
# for loop in range
"""
for (i=0; i<5; i++)     # i = 0,1,2,3,4
{

}
"""
# range(5) = 0,1,2,3,4
# for i in range(5):      # i = 0,1,2,3,4
#     print(i)

"""
for (i=-10; i<=10; i++)     # i = 0,1,2,3,4
{

}
"""
# for i in range(-10, 11):      # i = -10,-9,-8,....,0,1,2,3,4... 10
#     print(i)

"""
for (i=-10; i<10; i=i+2)     # i = 0,1,2,3,4
{

}
"""
# for i in range(-10, 10, 2):      # i = -10,-8, -6....,0,2,4... 8
#     print(i)

# pass, break & continue statements
# break will always break only one loop that comes first in the lineage.
"""
fruits = ["apple", "banana", "kiwi", "mango", "strawberry", "peach"]
for fruit in fruits:
    if fruit == "mango" or fruit == "banana":
        # break
        # continue
        pass
    print(fruit)
print("Thanks for eating fruits")
"""
# for else: (break - else)
# prime number:
# 1. Write a Python code that asks an integer to user and print whether it is prime or not.
"""
n = int(input("Enter the number you want to check: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")
"""
# 2. Write a Python code that takes 2 integers from user and prints all the prime numbers between them (including both).
"""
a = int(input("Enter two numbers:\n"))      # 95
b = int(input())                            # 200
print(f"Prime numbers between {a} and {b} (including both) are:")
for n in range(a, b+1):     # n = 95, 96, 97.... 200
    if n == 1:
        continue
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            break
    else:
        print(n, end="\t")
"""
"""
641:   2 to 640 
    => 2 to 321
    => 2 to 26
"""
# Write a Python program to create a user-defined list of fruits.
"""
n = int(input("How many fruits do you want to enter? "))
i = 0
fruits = []
print(f"Enter names of {n} fruits:")
while i < n:
    fruits.append(input())
    i += 1
print(fruits)
fruit = input("Enter the fruit you want to check: ")    # banana
if fruit in fruits:
    print("Present")
else:
    print("Not Present")
"""
# Write a Python code that takes a integer from user and prints whether that number is an Armstrong number or not.
"""
n = int(input("Enter an integer: "))    # 153 => [1, 5, 3] => [1^3, 5^3, 3^3] => sum(myList)

# digits = []
# for char in str(n):
#     digits.append(char)

digits = [int(char)**len(str(n)) for char in str(n)]
# print(digits)
if sum(digits) == n:
    print("Armstrong.")
else:
    print("Not Armstrong.")
"""
n = int(input("Enter an integer: "))
digits = [int(char)**len(str(n)) for char in str(n)]
print("Armstrong.") if sum(digits) == n else print("Not Armstrong.")
# Next Class: Functions, Modules & Packages