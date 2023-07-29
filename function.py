# function is a block of code which performs a specific task
# def function_name ();

def afternoon(firstname, lastname):
    print(f"hi{firstname}{lastname}")
    print("Afternoon are close to 100")


# calling a function
afternoon("Nsereko", "julius")

# arguents and parameters
# Arguments are specified after the function

# example 2


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)
print()

# return values


def my_function(w):
    return 5 * w


my_function(10)
