# 2. Take values of length and breadth of a rectangle from user and check if it is square or not.

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

if length == 0 and breadth == 0:
    print("It is Dot.")
elif length == 0 or breadth == 0:
    print("It is Line.")
elif length == breadth:
    print("It is Square.")
else:
    print("It is Rectangle.")

