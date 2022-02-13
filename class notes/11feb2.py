stock = []

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

    @classmethod
    def addNewCar(cls):
        print("-----------Welcome to add new car------------")
        print("Enter the following details:")
        name = input("Name: ")
        price = int(input("Price: "))
        fuel = input("Fuel: ")
        return cls(name, price, fuel)

stock.append(Car("Baleno", 800000, "Diesel"))
stock.append(Car("i20", 900000, "Petrol"))
# print(stock)
while True:
    print("Press 1 to add new car")
    print("Press 2 to see details of a car")
    print("Press 9 to exit")
    choice = int(input())
    if choice == 1:
        stock.append(Car.addNewCar())
    elif choice == 2:
        print("Serial numbers of cars in stock:")
        print("Sr.No.\tName")
        i = 0
        for car in stock:
            print(f"{i}\t{car.name}")
            i += 1
        subChoice = int(input("Which Car's details do you want to see? Enter serial number: "))
        stock[subChoice].printDetails()
    elif choice == 9:
        break
    else:
        print("Invalid Option, please try again...")
print("Thanks for using our car management system! See you soon!")

# Next class: Four Pillars of OOP: Inheritance, Polymorphism, Abstraction & Encapsulation, Exception Handling, File Handling