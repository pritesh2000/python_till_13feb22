"""
l1 = [1,2,3]
l2 = [200,300,400]
# l1 = [1,2,3,200,300,400]
l1.extend(l2)
print(l1)
name = "Python"
l1.extend(name)
print(len(l1))
print(l1)
"""
# Decision Making: if-else
"""
if (n > 0)
{
    printf("n is positive");
}
printf("Thanks for using our program");
"""
"""
number = float(input("Enter any number: "))
if number > 0:
    print("Your number is:", number)
    number = number * 2
    print(f"{number}'s double is positive")
elif number == 0:
# if number == 0:
    print(f"{number} is nuetral")
else:
# if number <= 0:
    print(f"{number} is negative")
print("Thanks for using our program")
"""
# shorthand notation for if-else
# independant if

# number = float(input("Enter any number: "))
"""
if number > 0:
    print(f"{number} is positive")
"""
# if number > 0: print(f"{number} is positive")

# if-else
# number = float(input("Enter any number: "))
"""
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
"""
# print(f"{number} is even") if number % 2 == 0 else print(f"{number} is odd")

# shorthand notation for if-elif-else is not available in Python

# Loops: while loop & for loop
"""
n = int(input("Enter any integer: "))       # 5
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
"""
"""
5 x 1 = 5
5 x 2 = 10
.
.
.
5 x 10 = 50
"""
"""
# Write a Python code that takes a integer from user and prints whether that number is an Armstrong number or not.
A 3 digit number is Armstrong number if sum of cubes of all its digits is equal to the number itself.
A 4 digit number is Armstrong number if sum of 4th power of all its digits is equal to the number itself.
A 5 digit number is Armstrong number if sum of 5th power of all its digits is equal to the number itself.
example:
151 is not Armstrong number:
1^3 = 1
5^3 = 125
1^3 = 1
----------
127 != 151

153 is an Armstron number:
1^3 = 1
5^3 = 125
3^3 = 27
----------
      153

1634 is an Armstrong number.
1^4 = 1
6^4 = 1296
3^4 = 81
4^4 = 256
----------
1634
"""
"""
n = int(input("Enter the number you want to test: "))
backup = n
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit ** len(str(backup))
    n = n // 10
if sum == backup:
    print("Armstrong")
else:
    print("Not Armstrong")
"""
"""
Write a Python code that asks an integer to user and print whether it is prime or not.
"""
"""
n = int(input("Enter an integer: "))
i = 2
prime = 1
while i < n:        # 15
    if n % i == 0:
        print("Not Prime")
        prime = 0
        break
    i += 1
if prime == 1:
    print("Prime.")
"""
"""
while - else = break - else
"""
"""
n = int(input("Enter an integer: "))
i = 2
while i < n:        # 25
    if n % i == 0:
        print("Not Prime.")
        break
    i += 1
else:
    print("Prime.")
"""
# Write a Python Program to create a user-defined list of fruits

"""
Write a Python program to create a user-defined list of fruits. Now ask user to enter any fruit of his/her choice. Print whether that fruit belongs to the list or not.
"""