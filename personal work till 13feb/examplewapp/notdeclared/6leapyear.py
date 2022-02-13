# 6. Write a Python program to find whether a given year is a leap year or not. 
# Test Data : 2016
# Expected Output :
# 2016 is a leap year.

year = int(input("Enter year: "))

if year % 4 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
