# 3. Write a Python code that takes an  integer from user and print all the factors of that integer.

n = int(input("Enter number :"))
i = 1
while n >= i:
    if n % i == 0:
        print(i)
    i += 1
