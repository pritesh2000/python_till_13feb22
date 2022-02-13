# 8. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
# Eligibility Criteria : 
# Marks in Maths must be atleast 65,
# Marks in Phy must be atleast 55,
# Marks in Chem must be atleast 50 and 
# Total marks all three subject must be atleast 190 or Total in Maths and Physics >=140 ------------------------------------- 
# Input the marks obtained in Mathematics :72 
# Input the marks obtained in Physics :65 
# Input the marks obtained in Chemistry :51 
# Total marks of Maths, Physics and Chemistry : 188 
# Total marks of Maths and Physics : 137 
# The candidate is not eligible.

mathematics = int(input("Input the marks obtained in Mathematics :"))
physics = int(input("Input the marks obtained in Physics :"))
chem = int(input("Input the marks obtained in Chemistry :"))
print(f"Total marks of Maths, Physics and Chemistry : {mathematics+ physics+ chem}")
print(f"Total marks of Maths and Physics : {mathematics + physics}")

if mathematics >= 65 and physics >= 55 and chem >= 50:
    if ((mathematics + physics + chem) >=190 ) or ((mathematics + physics) >= 140) :
        print("The candidate is eligible")
    else:
        print("The candidate is not eligible.")
else:
    print("The candidate is not aligible.")
