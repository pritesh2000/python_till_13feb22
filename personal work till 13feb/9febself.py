n= int(input("Enter how many fruits you want to enter?"))
i= 0
fruits = []
print(f"Enter names of {n} fruits:")
while i<n:
    fruits.append(input())
    i += 1
print(fruits)
fruit = input("Enter the fruit you want to check")
if fruit in fruits:
    print("present")
else:
    print("Not present")
    