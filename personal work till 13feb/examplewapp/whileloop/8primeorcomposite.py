# 8. Write a program that takes a number from user and prints whether it is prime or composite.

n = int(input("Enter number:"))
factor = 0
for i in range(2, n +1):
    if n % i == 0:
        # print("factor", i)
        factor += 1
    # else:
        # print(i)
if factor >= 2:
    print("Composite")
elif n == 1 or n == 0:
    print("Neither prime nor composite")
else:
    print("Prime")