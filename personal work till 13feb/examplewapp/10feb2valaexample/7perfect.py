# 7. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. 
# A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

a = int(input("Enter number for start : "))
b = int(input("Enter number for end : "))

def per(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if sum == n :
        return n

for x in range(a,b):
    if per(x) != None:
        print(per(x), end="\t")