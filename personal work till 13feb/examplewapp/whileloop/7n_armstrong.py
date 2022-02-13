# 7. An n-digit number is called Armstrong number if sum of nth powers of its all digits is equal to the number itself. Write a program that takes a number from user and prints whether it is an Armstrong number or not.

n = int(input("Enter number:"))
dlct = n
sum = 0

while n > 0:
    temp = n % 10
    sum = sum + temp ** len(str(dlct))
    n = n // 10
if dlct == sum:
    print("Armstrong")
else:
    print("Not Armstrong")
