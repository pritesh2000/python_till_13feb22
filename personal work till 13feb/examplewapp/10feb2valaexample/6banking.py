"""
6.Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""

user_name = []
user_password = []
user_balance = []


def create_account():
    user_name.append(input("Enter your name : "))
    user_password.append(input("Enter your password : "))
    user_balance.append(25000)    

def login():
    
    name = input("Enter username : ")
    password = input("Enter password : ")
    money = user_balance[user_name.index(name)]
    if name in user_name and password in user_password and user_name.index(name) == user_password.index(password):
        while True:
            
            print("\n1.Deposit")
            print("2.Withdraw")
            print("3.Check Balance")
            print("9.Logout")
            user_choice = int(input("Enter your choice : "))
            print()
            if user_choice == 1:
                deposit(name)
            elif user_choice == 2:
                withdraw(name)
            elif user_choice == 3:
                checkBalance(name)
            elif user_choice == 9:
                break
            else:
                print("Invalid choice...!!!\n")
    else:
        print("Username or password maybe incorrect !!!\n")

def deposit(name):
    # balance = money
    money = user_balance[user_name.index(name)]

    dep = int(input("Enter the amount you want to deposit : "))
    money += dep
    user_balance[user_name.index(name)] = money
    
    

def withdraw(name):
    money = user_balance[user_name.index(name)]

    wit = int(input("Enter the amount you want to withdraw : "))
    money -= wit
    
    if money < 10000:
        print("Insufficient Balance...\n")
    else:
        user_balance[user_name.index(name)] = money
        

def checkBalance(name):
    print(f"User name : {user_name[user_name.index(name)]}")
    print("Balance :", user_balance[user_name.index(name)])
    
while True:
    print("\n-----Welcome to Royal Bank-----")
    print("1.Create Account")
    print("2.Login")
    print("9.Exit")
    choice = int(input("Enter your choice : "))
    print()
    if choice == 1:
        create_account()
    elif choice == 2:
        login()
    elif choice == 9:
        break
    else:
        print("Invalid Choice...!!!\n")


