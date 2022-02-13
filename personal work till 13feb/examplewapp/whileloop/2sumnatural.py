# 2. ask an integer from user and print the sum of all the natural numbers till that integer.

n = int(input("Enter number:"))
i = 0
sum = 0
while n+1 > i:
    sum = sum + i
    i += 1

print(sum)