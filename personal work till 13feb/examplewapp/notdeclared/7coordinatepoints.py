# 7. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
# Test Data : 
# x-coordinate: 7
# y-coordinate: 9
# Expected Output :
# The coordinate point (7,9) lies in the First quadrant.

x = float(input("Enter x-coordinate : "))
y = float(input("Enter y-coordinate : "))

if x > 0 and y > 0:
    print(f"The coordinate point ({x},{y}) lies in the First quadrant.")
elif x < 0 and y > 0:
    print(f"The coordinate point ({x},{y}) lies in the Second quadrant.")
elif x < 0 and y < 0:
    print(f"The coordinate point ({x},{y}) lies in the Third quadrant.")
elif x > 0 and y < 0:
    print(f"The coordinate point ({x},{y}) lies in the Fourth quadrant.")
elif x == 0 and y == 0:
    print(f"The coordinate point ({x},{y}) lies in section point of x and y axis.")
elif x == 0 :
    print(f"The coordinate point ({x},{y}) lies in y axis.")
elif y == 0 :
    print(f"The coordinate point ({x},{y}) lies in x axis.")
else:
    print("Invalid input!!!")
    