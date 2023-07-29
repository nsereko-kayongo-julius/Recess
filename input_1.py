# input and output
# input ('prompt')

name = input("what is your name? \n")
print("my name is: " + name)

# example 2
number = int(input("whatnumber do you want to double.."))
double = 2*number
print(f"your number has been doubled to {double}")

# multiple input


# taking four inputs at a time
a, b, c, d = input("Enter four values: ").split()
print("First number is {}, second number is {} third is {} and fourth is {}".format(a, b, c, d))
print()

# using the list() and map() method
my_tuple = (2, 3, 4, 5)
print(my_tuple)
list_of_numbers = list(my_tuple)
list_of_numbers.append(int(input("enter a list of numbers ")))
list_to_tuple = tuple(list_of_numbers)
print(list_to_tuple)
print()

list2 = list(map(int, input("enter a list of values ").split()))
print(list2)
print(type(list2))
print()

my_set1 = set(map(int, input("enter a set of values ").split()))
print(my_set1)
print(type(my_set1))
