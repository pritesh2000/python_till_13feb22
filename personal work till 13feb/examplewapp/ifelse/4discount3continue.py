"""
4. In program-3, ask user for his/her name, mobile number, quantity and price of each item, then decide whether he/she is eligible for discount and based on that print the invoice in the following format:
case 1- when customer is not eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              50          3               150
item-2              100         4               400
item-3              40          5               200
                                                ---------
                                Final Amount:   750 
----------------Thanks for shopping with us!---------------

case 2- when customer is eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              90          3               270
item-2              100         4               400
item-3              40          10              400
                                                ---------
                                Grand Total:    1070
                                Discount:        107
                                                ---------
                                Final Amount:    963
----------------Thanks for shopping with us!---------------
"""

cust = input("Enter your name: ")
mobile_num = int(input("Enter your mobile number: "))
item = int(input("Enter how many item you want to purchase: "))

price = []
qty = []
total = []

for i in range(item):
    price.append(int(input(f"Enter price of item-{i+1}: ")))
    qty.append(int(input(f"Enter quantity of item-{i+1}: ")))
    
for i in range(item):
    total.append(price[i]*qty[i])

print("---------------------Retail Invoice---------------------")
print(f"Customer Name: {cust}")
print(f"Contact Number: {mobile_num}")
print("Date of Invoice: 11-02-2022")
print("--------------------------------------------------------")
print("Items\tPrice\tQuantity\tTotal".expandtabs(16))

for i in range(item):
    print(f"item-{i+1}\t{price[i]}\t{qty[i]}\t{total[i]}".expandtabs(16))
print("\t\t\t---------".expandtabs(16))


if sum(total) <= 1000:          
    print(f"\t\tFinal Amount:\t{sum(total)}".expandtabs(16))

else:
    print(f"\t\tGrand Total:\t{sum(total)}".expandtabs(16))
    print(f"\t\tDiscount:\t {int(sum(total)/10)}".expandtabs(16))
    print("\t\t\t---------".expandtabs(16))
    print(f"\t\tFinal Amount:\t {sum(total)-int(sum(total)/10)}".expandtabs(16))

print("--------------Thanks for shopping with us!--------------")
