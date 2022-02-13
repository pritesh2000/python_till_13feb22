"""
Operators in Python
1. Arithmetic
    +
    -
    *
    /
    %
    //      Floor Division
    **      Exponent

2. Comparision/Conditional/Relational Operators/Condition
    These operators will always return either True or False
    <
    >
    <=
    >=
    ==      Equality check
    !=

3. Logical Operators
    and : For successful login, user must enter both the username as well as password correctly.
        
        c1  c2  c1 and c2
        0   0   0
        0   1   0
        1   0   0
        1   1   1

    or : To signup, user must enter either his email address or mobile number.
    
        c1  c2  c1 or c2
        0   0   0
        0   1   1
        1   0   1
        1   1   1

    not: Do not write your name on answer sheet.

        c1  ok?
        1   0
        0   1

4. Bitwise operators:
    &   Bitwise and
        3 : 0 0 1 1
            & & & &
        5 : 0 1 0 1 
        -----------
            0 0 0 1 : 1

    |   Bitwise or
        3 : 0 0 1 1
            | | | |
        5 : 0 1 0 1 
        -----------
            0 1 1 1 : 7

    ~   Bitwise not
        5 : 0 1 0 1
        ~5: 1 0 1 0 = -6

    ^   Exclusive or (xor)
        3 : 0 0 1 1
        ^   ^ ^ ^ ^
        5 : 0 1 0 1
        -----------
            0 1 1 0

    <<  left shift
        22 : 0 0 0 1  0 1 1 0
        << : 0 0 1 0  1 1 0 0
        << : 0 1 0 1  1 0 0 0
        << : 1 0 1 1  0 0 0 0

    
    >>  right shift
        180 : 1 0 1 1  0 1 0 0
        >>  : 0 1 0 1  1 0 1 0  = 90
        >>  : 0 0 1 0  1 1 0 1  = 45
        >>  : 0 0 0 1  0 1 1 0  = 22

5. Assignment Operators
    =   Assignment
        a = 5
        5 + 7 = x
        x = 5 + 7

    shorthand operators
    a = a + b   =>  a += b
    a = a - b   =>  a -= b
    a = a * b   =>  a *= b
    a = a / b   =>  a /= b
    a = a % b   =>  a %= b
    a = a // b   =>  a //= b
    a = a ** b   =>  a **= b
    a = a & b   =>  a &= b
    a = a | b   =>  a |= b
    a = a ^ b   =>  a ^= b
    a = a << b   =>  a <<= b
    a = a >> b   =>  a >>= b

        * There is no such thing as a++ or a-- or ++a or --a in Python.

6. Membership Operators
    in
    not in

7. Identity Operators
    is
    is not

"""
print(15/4)
print(15//4)
print(15 ** 4)
print(3 > 6)
print(3 > 6 or 5 < 7)
print(3 | 5)
print(~5)
print(22 << 3)
print(180 >> 2)
print(180 >> 3)
name = "Mayur Solanki"
print("n" in name)
print("m" in name)

numbers = [11, 22, 33, 22, 44, 22, 67, 99, 22, -4006, 9898, 0, -33, 22]
n2 = numbers.copy()
n3 = numbers
print(n3 is numbers)
print(n2 is numbers)
print(n2 == numbers)

# class: string in extend, decision making, loops