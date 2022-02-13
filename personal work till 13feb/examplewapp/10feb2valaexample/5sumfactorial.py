# 5.Make a Python program that asks 5 numbers from user, finds their factorials using a function that takes 1 number in its argument & returns its factorial, adds all the factorials returned by function & prints the final answer on the screen.

user_num = []

def fact(n):
    if n== 0 :
        return 1
    else:
        return n * fact(n-1)

for i in range(5):
    user_num.append(fact(int(input())))

print("Sum of all number's factorial is ", sum(user_num))
