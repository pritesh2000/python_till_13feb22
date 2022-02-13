# collections in python
"""
    Mutable     Ordered     list    -   []
    Immutable   Ordered     tuple   -   ()
    Mutable     Unordered   set     -   {}
    Immutable   Unordered   frozenset   {}

Two special collections:
string: Collection of characters    :   Immutable & Ordered     -   ""
dictionary: Collection of key-value pairs   :   Mutable & Unordered -   {}
"""
# Tuples: Immutable & Ordered collection of members
"""
t1 = ("Ahmedabad", "Bangalore", "Pune", "Nasik")
l1 = ["Ahmedabad", "Bangalore", "Pune", "Nasik"]
# index:    0           1           2       3
# -ve index:-4          -3          -2      -1
print(t1[2])
l1[2] = "Mumbai"
print(l1)
# t1[2] = "Mumbai"      tuples are immutable!
print(t1[-2])
# slicing is exactly the same as in string/list
print(t1[1:3])
"""
# Another way to create a tuple
"""
t2 = 11,22,33,44,33,22,11,55,77,44,22
print(t2)
print(type(t2))
print(len(t2))
print(min(t2))
print(max(t2))
print(sorted(t2))
"""
# creating single element tuple
"""
t3 = (45)
print(t3)
print(type(t3))
t4 = ("Delhi")
print(t4)
print(type(t4))
t3 = (45,)
print(t3)
print(type(t3))
t4 = ("Delhi",)
print(t4)
print(type(t4))
t5 = 95,
print(t5)
"""
# Unpacking of collections:
"""
student_data = ("Neeraj", 19, "male")
# name = student_data[0]
# age = student_data[1]
# gender = student_data[2]
# print(f"Name:\t{name}\nAge:\t{age}\nGender:\t{gender}")
name, age, gender = student_data
print(f"Name:\t{name}\nAge:\t{age}\nGender:\t{gender}")
"""
# student_data = ("Neeraj", 19, "male", "Javeline", "68", "India")

# name, age, *other_details = student_data
# print(f"Name:\t{name}\nAge:\t{age}\nOthers:\t{other_details}")

# *others, weight, country = student_data
# print(f"Weight:\t{weight}\nCountry:\t{country}\nOthers:\t{others}".expandtabs(10))

# name, *others, country = student_data
# print(f"Name:\t{name}\nCountry:\t{country}\nOthers:\t{others}".expandtabs(10))

# name, *others1, hobby, *others2 = student_data    Error

# for loop with multiple variables
"""
data = [
    ("Neeraj", 98, "Physics"),
    ("Rohit", 96, "Maths"),
    ("Dhoni", 94, "Computers")
]
for student, marks, subject in data:
    print(f"{student} got {marks} marks in {subject}")
"""
# methods of tuple
"""
t1 = (22, 33, 11, 22, 88, 44, 66, 22)
print(t1.count(22))
print(t1.index(88))
print(t1.index(22))
print(t1.index(22,4))
print(t1.index(22, 1, 5))
"""

# list1 = [
#     [2, 3 ,7],
#     [4, 2, -5],
#     [7, 8, 9]
# ]
# print(list1)
# print(list1[1][2])

"""
list2 = ["Ahmedabad is a nice city with lots of dirt and dust.", "Pune is comparatively colder than Mumbai.", "Gandhinagar is a green city.", "Bhavnagar is famous for Ganthiya."]
print(list2[2][5:15:2])
print(list2[0].upper())
"""

# =====================================Sets===========================================

# set: Mutable & Unordered collection of members in which repeatition is eliminated.
"""
s1 = {35, 55.44, 98, 12, 23, 67, 9, 9, 9}
# No index numbers
# No negative index
# No slicing
# No accessing through index
# No first element, no last element
# s1[3] = 21
# s1.add(9)
# s1.add(9)
# s1.add(9)
print(s1)
print(type(s1))
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
student_data = {"Neeraj", 19, "male", "Javeline", "68", "India"}
name, age, *others = student_data
print(f"Name:\t{name}\nAge:\t{age}\nOthers:\t{others}")

s3 = {}
print(s3)
print(type(s3))
d = {"Maths":98, "Physics":92, "Chemistry":78}
"""
# Creating empty set
"""
s4 = set()
print(s4)
print(type(s4))
print(len(s4))
"""
# s1 = {35, 55.44, 98, 12, 23, 67, 9, 9, 9}
"""
s1.add(10)
s1.clear()
s2 = s1.copy()
s3 = s1
"""
# s1.discard(55.44)
# print(s1.discard(100))
# print(s1.remove(100))
# print(s1.remove(35))
# print(s1.pop())
# print(s1)

# s2 = {101, 201, 301, 98}
# s1.update(s2)
# print(s1)
"""
s1 = {1,2,3,4,5,6}
s2 = {3,4,5,6,7,8}
s3 = {7,8,9,10,11}
s4 = {i for i in range(1, 16)}

a = s1.union(s2)
print(a)
b = s1.intersection(s2)
print(b)
c = s1.difference(s2)
d = s2.difference(s1)
print(c)
print(d)
e = s1.symmetric_difference(s2)     # (s1-s2) U (s2-s1)
f = s2.symmetric_difference(s1)     # (s2-s1) U {s1-s2}
print(e)
print(f)
print(s1.issubset(s4))
print(s4.issuperset(s1))
print(s1.intersection(s3))
print(s1.isdisjoint(s3))
"""
"""
s1.intersection_update(s2)
# same as s1 = s1.intersection(s2)
print(s1)
"""
# s1.difference_update(s2)
# print(s1)

# s1.symmetric_difference_update(s2)
# print(s1)

# s1.update(s2) works like s1.union_update(s2) so we don't have union_update method.
"""
l1 = [
    12, 12.34, 5 + 7j,
    "string",
    [1,2,3],
    (4,5,6),
    {7,8,9}
]
print(l1)
t1 = (
    12, 12.34, 5 + 7j,
    "string",
    [1,2,3],
    (4,5,6),
    {7,8,9}
)
print(t1)
s1 = {
    12, 12.34, 5 + 7j,
    "string",
    # [1,2,3],
    (4,5,6),
    # {7,8,9}
}
print(s1)
"""
# We can not nest mutable collection in unordered collection in Python

# frozenset: Immutable version of set
"""
s1 = {1,2,3,4,5,6}
s2 = {3,4,5,6,7,8}
s3 = {7,8,9,10,11}
fs1 = frozenset(s1)
fs2 = frozenset({1,2,3,4})
fs3 = frozenset([5,6,7,8])
fs4 = frozenset((5,6,7,8))
print(fs1, fs2, fs3, fs4)
"""
# frozensets have all the methods of sets except those which were modifying the original set.

# After Break: Dictionaries, functions, Modules & Packages
# Dictionaries: Mutable & Unordered collections of key-value pairs
"""
d1 = {"Maths":98, "Physics":92, "Chemistry":78}
print(d1["Physics"])
# Methods of dictionaries:
# d1.clear()
# d1.copy()
l1 = ["Hitesh", "Mahesh", "Ketan", "Parag"]
d2 = dict.fromkeys(l1, 1000)
print(d2)
print(d1.get("Maths"))
print(d1.get("Computers"))
# print(d1["Computers"])        Error
print(d1.keys())
print(d1.values())
print(d1.items())
"""
# for loop in dictionary:
"""
for x in d1:            # as good as for x in d1.keys()
    print(x)
for x in d1.values():
    print(x)
for x in d1.items():
    print(x)

print("Subject\tMarks".expandtabs(16))
for a,b in d1.items():
    print(f"{a}\t{b}".expandtabs(16))
"""
"""
print(d1.pop("Physics"))
print(d1)

print(d1.popitem())
print(d1)
"""
"""
d1.update(d2)
print(d1)
"""
"""
d1["Computer science"] = 100
print(d1)

d1["Computer science"] = 99
print(d1)

print(d1.setdefault("Computer science", 98))
print(d1)

print(d1.setdefault("Biology", 89))
print(d1)
"""
"""
Write a Python code to create a user-defined dictionary in which keys are names of people and their values will be food ordered by them.
"""
d = {}
temp = True
while temp != "x" and temp != "X":
    name = input("Enter name of the next person: ")
    food = input("His food: ")
    ret = d.setdefault(name, food)
    if ret == food:
        print("Success!")
    else:
        print(f"Oops! Key {name} already exist with value {ret}. Do you want to overwrite?")
        choice = input("y or n? ")
        if choice == "y" or choice == "Y":
            d[name] = food
            print("Key-value pair overwritten.")
        else:
            print("Key-value pair could not be updated...")
    temp = input("Enter 'x' to finish or any other key to enter more people: ")
print(d)