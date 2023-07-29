import tkinter as tk
from tkinter import *
# Basic operators
"""
Arithetic operator

+ - * / // % ** 
--Comparison operators
< <= > >= == !=
--logical operators
Logical AND: and 
Logical OR: or 
Logical NOT: not

--Assignment operators
Assign value : =
Add value : +
Add and assign value : += 
Subtract and assign value : -= 
multiply and assign value : *= 
divide and assign value : /= 
 and assign value : //= 
modulo and assign value : %= 
power and assign value : **=

--member operators
Member operators : in checks if a value  is a member of a sequence
Member operators : not in checks if a value is not a member of a sequence

--identity operators
Identity operators : is checks if a two values are identical
Identity operators : is not checks if two values are not identical 
"""
# example
import tkinter as tk
a = 10
b = 20
# Addition
print(a + b)

# Subtraction
print(a - b
      )
# Multiplication
print(a * b)

# Division
print(a / b)

# Floor division
print(a // b)

# Modulo
print(a % b)

# Power
print(a ** b)

# Comparison operators
# greaterThan
if a > b:
    print("a is greater than b")
    print(a > b)

# lessThan
if a < b:
    print("a is less than b")
    print(a < b)

# greaterThanEqual
if a >= b:
    print("a is greater than or equal to b")
    print(a >= b)

# lessThanEqual
if a <= b:
    print("a is less than or equal to b")
    print(a <= b)

# Identity operators
x = True
y = False

# logical AND
print(x and y)

# logical OR
print(x or y)

# logical NOT
print(not x)
print(not y)

# Assignment operators
w = 5
# Add and assign
w += 5
print(w)
# Subtract and assign
w -= 5
print(w)
# multiply and assign
w *= 5
print(w)
# divide and assign
w /= 5
print(w)

# modulus and assignment
w %= 5
print(w)

# power and assignment
w **= 5
print(w)

# Member
lakes = ["Victoria", "Kyoga", "Albert", "Edward", "George"]
if "Kyoga" in lakes:
    print("Kyoga is a lake")


# not in
lakes = ["Victoria", "Kyoga", "Albert", "Edward", "George"]
if "Kyoga" not in lakes:
    print("Kyoga is not a lake")

# Identity operators
x = True
y = False
print(x is y)
print(x is not y)


# Identity operators
x = True
y = False
print(x == y)
print(x != y)


# bitwise operators
"""
Bitwise operators are used to perform operations on individual bits in of binary numbers.
Bitwise AND (&): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR (1): Performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR (^): Performs a bitwise XOR operation
Bitwise NOT (-): Performs a bitwise NOT operation between the corresponding
Bitwise left shift ('<<): Performs a bitwise left shift operation
Bitwise right shift (>>): Performs a bitwise right shift operation
"""

# example
a = 10
b = 20
# Bitwise AND
print(a & b)

# calcutor app
number1 = float(input('Enter first number: '))
op = input('Enter operator (+,-,*,/,^): ')
number2 = float(input('Enter second number: '))
print(number1, op, number2)


def calculate(n1, n2, op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result = n1*n2
    elif op == '/':
        result = n1/n2
    elif op == '^':
        result = n1**n2

    return result


def calculate(n1, n2, op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result = n1*n2
    elif op == '/':
        result = n1/n2
    elif op == '^':
        result = n1**n2

    return result


result = calculate(number1, number2, op)
print('=', result)
