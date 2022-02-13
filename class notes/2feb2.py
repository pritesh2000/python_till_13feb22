s0 = "Students of"
s1 = "this batch is going to ROCK the software industry."
s2 = s0 + " " + s1
a = 3 + 5 + 8
# s1.__add__
# a.__add__

# case related methods:
"""
print("capitalize: ", s1.capitalize())
print("up", s1.lower())
print("swapcaseper:", s1.upper())
print("lower::", s1.swapcase())
print("title:", s1.title())
print("casefold:", s1.casefold())

s3 = "What is ß"
print(s3.lower())
print(s3.casefold())

print(s1)
"""
# Allignment related methods
"""
s4 = "Welcome to Royal."
s5 = s4.center(100)
print(len(s4))
print(len(s5))
print(s4.center(100, "$"))
print(s4.center(20, "$"))

s6 = "Welcome to Royal"
print(" " + "="*98)
print("|" + s6.center(98) + "|")
print(" " + "="*98)

print(s4.rjust(100))
print(s4.rjust(100, "#"))

print(s4.ljust(50, "*"))

"""
# count
"""
print(s1.count("i"))
print(s1.count("i", 10))
print(s1.count("i", 10, 20))
print(s1.count("i", 12, 13))

print(s1.count("is"))
print(s1.count("in", 20))
print(s1.count("in", 10, 20))
"""

# print(s1.encode())

# startswith & endswith
"""
s0 = "Students of"
s1 = "this batch is going to ROCK the software industry."
print(s0.startswith("Student"))
print(s1.endswith("industry"))
print(s1.startswith("bat", 5))
print(s1.endswith("industry", 0, -1))
"""

# expandtabs
"""
s5 = "Let's\textend\ttoday's\tlectures\ttill\t4pm"
print(s5)
print(s5.expandtabs(15))

print("Subject\t\tmarks")
print("Physics\t\t73")
print("Chemistry\t\t89")
print("Environmental Science\t\t78")
print("Computer Science\t\t98")
print("English\t\t68")
print()

print("Subject\tmarks".expandtabs(30))
print("Physics\t73".expandtabs(30))
print("Chemistry\t89".expandtabs(30))
print("Environmental Science\t78".expandtabs(30))
print("Computer Science\t98".expandtabs(30))
print("English\t68".expandtabs(30))
"""
# Next class: methods starting with f