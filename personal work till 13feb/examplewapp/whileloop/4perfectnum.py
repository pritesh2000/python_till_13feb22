# 4. A number is called perfect number if sum of all its factors (except itself) is equal to the number itself. Write a program that takes an integer from user and print whether it is a perfect number or not.

n = int(input("Enter number :"))
m = n
i = 1
sum = 0
while n > i:
    if n % i == 0:
        print(i)
        sum = sum + i
    i += 1
if m == sum:
    print("Number is Perfect number")
else:
    print("Number is not perfect number")