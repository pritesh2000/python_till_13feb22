# OOP: Object Oriented Programming - Data Oriented
"""
Class: Hypothetical: Humans, Men, Women, Girl, Boy, Car, Furniture
Object: Tengible: Alakh, Urmi, BMW, Chair, Sofa
"""
# s1 = "Today is Friday"
# print(type(s1))
# s1.upper()
# s1.append(".")

class Car:
    wheels = 4          # class variable
    seating_capacity = 5
    
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
    
    def printDetails(self):
        print(f"---------Details of {self.name}---------")
        print(f"Name:\t{self.name}")
        print(f"Price:\t{self.price}")
        print(f"Fuel:\t{self.fuel}")
        print(f"Wheels:\t{self.wheels}")
        print(f"Seats:\t{self.seating_capacity}")
        print("---------x---------x---------")

"""
c1 = Car()
c1.name = "Baleno"      # Object Variables
c1.price = 800000
c1.fuel = "Petrol"

# print(f"Name:\t{c1.name}")
# print(f"Price:\t{c1.price}")
# print(f"Fuel:\t{c1.fuel}")
# print(f"Wheels:\t{c1.wheels}")

c2 = Car()
c2.name = "i20"
c2.price = "900000"
c2.fuel = "Diesel"

c3 = Car()
c3.name = "XUV500"
c3.price = 2000000
c3.fuel = "Diesel"
c3.seating_capacity = 7

c1.printDetails()
c2.printDetails()
c3.printDetails()
print(c1.__dict__)
print(c3.__dict__)
"""
c1 = Car("Baleno", 800000, "Petrol")
c2 = Car("i20", 900000, "Diesel")
c3 = Car("XUV500", 2000000, "Diesel")
c3.seating_capacity = 7
c1.printDetails()
c2.printDetails()
c3.printDetails()