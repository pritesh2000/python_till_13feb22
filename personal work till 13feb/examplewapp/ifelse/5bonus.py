# 5. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and years of service and print the final salary.

emp_salary = int(input("Enter your salary: "))
emp_year = int(input("Enter your service: "))

if emp_year > 5:
    print(f"You will got {emp_salary * .05} bonus from company.")
    print(f"Your final salary will be {emp_salary * .05 + emp_salary}")
else:
    print("You have to spent some more year to get bonus.")
