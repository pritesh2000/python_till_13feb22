# 6. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

school_mark = int(input("Enter your marks: "))

if school_mark > 80 :
    print("Grade A")
elif school_mark > 60 :
    print("Grade B")
elif school_mark > 50 :
    print("Grade C")
elif school_mark > 45 :
    print("Grade D")
elif school_mark >= 25 : 
    print("Grade E")
else:
    print("Grade F")
