"""
0.Write a Python code to create a 3x3 matrix using nested lists, with values given by user. Also print it in a way that it looks like a matrix.
Next, upgrade your program for the dimension n x n where n is given by user.
"""

# --------------doubt here-----------

a = int(input("Enter number of row for matrix: "))
b = int(input("Enter number of column for matrix: "))

row = []
col = []
for r in range(a):
    for column in range(b):
        col.append(int(input()))
        print(col)

    row.append(col)
    col = []
    # col.clear()     # it is not working 
    print(col)
    print(row)

for i in range(len(row)):
    print(row[i])

