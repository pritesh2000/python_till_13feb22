numbers = [11, 22, 33, 22, 44, 22, 67, 99, 22, -4006, 9898, 0, -33, 22]
print(numbers.append(101))
print(numbers)
"""
print("Enter five members to store in list:")
list1 = []
list1.append(input())
list1.append(input())
list1.append(input())
list1.append(input())
list1.append(input())
print(list1)
"""
"""
numbers.clear()
print(numbers)
del numbers
print(numbers)
"""
"""
n2 = numbers.copy()
print("Numbers:", numbers)
print("n2:", n2)
n3 = numbers
print("n3:", n3)
numbers.clear()
print("n3:", n3)
n3.append(1000)
print("Numbers:", numbers)
print("n2:", n2)
del numbers
print("n3:", n3)
"""
"""
print(numbers.count(22))
# print(numbers.count(22, 4, 10))       Error
print(len(numbers))
l2 = ["USA", "India", "UK"]
# numbers.append(l2)
# print(len(numbers))
# print(numbers)
numbers.extend(l2)
print(numbers)
print(len(numbers))
"""
"""
print(numbers.index(99))
print(numbers.index(22))
print(numbers.index(22, 2, 7))
"""
print(numbers.insert(7, "Bangalore"))
print(numbers)

print(numbers.pop())
print(numbers)

print(numbers.pop(7))
print(numbers)

# print(numbers.pop(27))        indexError

print(numbers.remove(99))
print(numbers)

print(numbers.remove(22))       # removes the first occurance only
print(numbers)

print(numbers.reverse())
print(numbers)

numbers.sort()
# sorted(numbers)
print(numbers)
numbers.reverse()
print(numbers)