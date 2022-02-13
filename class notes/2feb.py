"""
Write a Python program that takes 5 integers (a, b, c, d and e) from user, finds their average and print the final output exactly as below:
Sample Execution:
Enter five integers:
3
4
5
6
7
Output:
The average of 3, 4, 5, 6 and 7 is: 5.0

not allowed:
The average of a, b, c, d and d is: 5.0
5.0
The average of 3 , 4 , 5 , 6 and 7 is: 5.0
"""
"""
print("Enter five integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = (a+b+c+d+e)/5
# print("The average of", a, "\b,", b, "\b,", c, "\b,", d, "and", e, "is:", avg)
# f-string
print(f"The average of {a}, {b}, {c}, {d} and {e} is: {avg}")
"""
# collections in python
"""
    Mutable     Ordered     list
    Immutable   Ordered     tuple
    Mutable     Unordered   set
    Immutable   Unordered   frozenset

Two special collections:
string: Collection of characters    :   Immutable & Ordered
dictionary: Collection of key-value pairs   :   Mutable & Unordered
"""
"""
# string: ordered & immutable collection of characters
s1 =    "This batch is going to rock the software industry."
# index: 0123456789.......................................49
# -ve: -50........................................987654321
print(s1)
print(type(s1))
print(len(s1))
print(s1[15])
# s1[15] = "O"          strings are immutable
s2 = s1[8:45]
print(s1)
print(s2)
print(s1[:20])
print(s1[10:])
print(s1[:])
# print(s1[550])        Error
print(s1[5:550])
print(s1[3:45:2])
print(s1[4:48:4])
print(s1[49])
"""
s1 =    "This batch is going to rock the software industry."
# -ve: -50........................................987654321
"""
print(s1[-1])
print(s1[-5])
print(s1[45])
print(s1[0])
print(s1[-40:-10])
# print(s1[-10:-40])    Null string
print(s1[::])
print(s1[::-1])
print(s1[-10:-40:-1])
print(s1[-10:-40:-3])
"""
"""
print(s1[6:-8])
print(s1[6:-8:2])
print(s1[6:-8:200])
"""
# Methods vs Functions
# string methods
x = 6
type(s1)
type(x)
y = 8.9
type(y)
# len(string)
# len(list)
# len(set)
# len(tuple)
# len(frozenset)
# len(dictionary)
z = 1.5
# len(z)
s1.capitalize()