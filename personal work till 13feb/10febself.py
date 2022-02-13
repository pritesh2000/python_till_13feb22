dict1 = dict()
n = int(input("How many customers are there ? write number"))
for i in range(n):
    name = input("Enter your name:")
    food = input("Enter food you want to order:")

    dict1[name] = food
print(dict1)
