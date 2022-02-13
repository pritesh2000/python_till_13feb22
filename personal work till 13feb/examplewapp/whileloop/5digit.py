# 5. Write a program to check number of digits in a given number.

n = int(input("Enter number :"))
i = 0
while n > 0:
    n = n // 10
    i += 1
print("Number of digit is", i)
