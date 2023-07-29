# function is a block of code which performs a specific task
# def function_name ();

# import nanyonga_rahmah_evening


import math


def afternoon(firstname, lastname):
    print(f"hi{firstname}{lastname}")
    print("Afternoon are close to 100")


# calling a function
afternoon("Nanyonga", "RAhmah")

# arguents and parameters
# Arguments are specified after the function

# example 2


def add(x, y):
    return x + y


print(add(1, 2))
print(add(1, 3))
print(add(2, 2))
print("-----------------")

# A simple calculator


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


# print(nanyonga_rahmah_evening.add(1, 2))

# import math odule and print the square root of a number

z = math.sqrt(64)

print(z)
# input and output
# input ('prompt')

name = input("what is your name?")
print("my name is: " + name)

# example 2
number = int(input("what is your number"))
percent = number / 100
print(f"your percentage is {percent}")

# multiple input

# split() breaks the input with space
a, b, c = input("Enter three values: ").split()
print("your values are", a, b, c)

my_tuple = (2, 3, 4, 5)
print(my_tuple)
my_list = list(my_tuple)
my_list.append(int(input("enter a number")))
w = tuple(my_list)
print(w)

my_list1 = list(map(int, input("enter multiple values").split()))
print(my_list1)
print(type(my_list1))

my_set = set(map(int, input("enter a set of values").split()))
print(my_set)
print(type(my_set))
