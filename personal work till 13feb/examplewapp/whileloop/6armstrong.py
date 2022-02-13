# 6. A 3-digit number is called Armstrong number if sum of cubes of its all digits is equal to the number itself. Write a program that takes a 3 digit number from user and prints whether it is an Armstrong number or not.

n = int(input("Enter 3 digit number:"))
sum = 0
m = n
while n > 0:
    temp = n % 10
    sum = sum + temp ** 3
    n = n // 10
if sum == m:
    print("Armstrong")
else:
    print("Not Armstrong")
