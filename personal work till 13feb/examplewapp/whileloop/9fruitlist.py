# 9. Ask user how many fruits does she want to add in a list. Then create a list with those many fruits given by user. (Create a Python code to generate user-defined list)

n = int(input("How many fruit you want to add in list:"))
fruits = list()
for i in range(n):
    fruits.append(input(f"{i + 1} : "))
print(fruits)