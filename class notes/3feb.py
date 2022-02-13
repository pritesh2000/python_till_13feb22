s1 =    "this batch is going to ROCK the software industry"
# index: 0123456789.......................................49
"""
print(s1.find("y"))
print(s1.find("i"))
print(s1.find("ROCK"))
print(s1.find("i", 3))
print(s1.find("i", 12, 20))
print(s1.find("z"))
print(s1.find("ing", 25, 40))

print()
print(s1.index("y"))
print(s1.index("i"))
print(s1.index("ROCK"))
print(s1.index("i", 3))
print(s1.index("i", 12, 20))
"""
# print(s1.index("z"))
# print(s1.index("ing", 25, 40))

# methods starting with 'is' will return either True or False
"""
print(s1.isalpha())
s2 = "DixitKava"
print(s2.isalpha())
s3 = "Dixit987654321"
print(s3.isalnum())
print(s2.isalnum())
s4 = "987654321"
print(s4.isalnum())
s5 = ""
print(s5.isalnum())
print(s5.isalpha(), "\n")

print(s4.isdecimal())       # allows only digits 0 to 9 nothing else
print(s4.isdigit())     # allows circled numbers, superscript, subscript
print(s4.isnumeric())   # allows roman numerals, vulgar fraction, digits from other languages
"""
"""
s6 = "5¹"
print(s6.isdecimal())
print(s6.isdigit())

s7 = "②⓪"

print(s7.isdecimal())
print(s7.isdigit())
print(s7.isnumeric())

s8 = "¼"

print(s8.isdecimal())
print(s8.isdigit())
print(s8.isnumeric())

s9 = "二千二十二"
print(s9.isdecimal())
print(s9.isdigit())
print(s9.isnumeric())
"""
# s2 = "ifforwithiswhile"
# print(s2.isidentifier())

# Case checking methods
"""
print(s1.islower())
print(s1.isupper())
print(s1.istitle())

s3 = "Shivam\tSingh"
print(s3.isprintable())
print(s1.isprintable())

s4 = "     \t\n   \n\n  \t\t"
print(s4.isspace())
"""

# s2 = s1.split()
# print(s2)
"""
print(s1.split("i"))
print(s1.split("i", 2))

print(s1.rsplit("i", 2))
"""
s3 = "#"
"""
print(s3.join(s2))
print("$".join(s2))
print(" ".join(s2))
"""
"""
s4 = "##########################Happy Birthday to you!!#######################"
s5 = s4.lstrip("#")
s6 = s4.rstrip("#")
s7 = s4.strip("#")
print(s5)
print(s6)
print(s7)

print(s1.partition("ROCK"))
print(s1.partition("in"))
print(s1.rpartition("in"))

print(s1.rfind("i"))
print(s1.rindex("is"))
# Explore other options in rfind and rindex

print(s1.replace("in", "OUT"))
print(s1.replace("in", "OUT", 1))
"""
"""
example:
s2 = s1[::-1]
s2 = s2.replace("ni", "TUO", 1)
s2 = s2[::-1]
print(s2)
"""
s3 = "Happy New Year!\nMay this year brings you health, wealth and happiness!\nForward this message to 3 of your close friends!"
# print(s3)
# print(s3.splitlines())

"""
write a Python program that takes a date and month number of 2022 and print it in dd-mm-yyyy format
"""
date = input("Enter today's date: ")
month = input("Enter month number: ")
print(f"Today's date: {date.zfill(2)}-{month.zfill(2)}-2022")