# Regular expression
# regex re.match(), re.search(), re.findall()

# Example 1 re.match(){match first word , match group word, match all numbers}

import re
txt = "hello my name is Nsereko am in year2 recess"
# search for the first word in the string
x = re.search(r"^\w+", txt)
print(f"The first word: {x.group()}")

# emailvalidate


def validate_email(email):
    if re.search(r"^\w+@\w+\.\w+$", email):
        print("Valid email")
    else:
        print("Invalid email")


# emails to validate
email1 = "nserekojulius@gmail.com"
validate_email(email1)

print()

# generators and iterrators
# iterators are objects used to iterrate over a collection of items
# iterrator object must implement two special methods __iter__() and __next__()

list1 = ['25', '2', 'coding', 'is', 'fun']
a = iter(list1)
# printing the itterator
print(a)

# print the first item
print(next(a))

# print all numbers in the iterrator
for item in a:
    print(item)

print()


numbers = range(1, 11)
iterator = iter(numbers)


for number in iterator:
    print(number)
print()


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print(number)


# decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        func(*args, **kwargs)
        print("After calling the function")
    return wrapper


@my_decorator
def hello_world():
    print("Hello, world!")


hello_world()
