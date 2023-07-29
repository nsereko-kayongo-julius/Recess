# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

"""
try to open a file(for reading) that does not exist (FileNotFoundError)
try to divide a number by zero (ZeroDivisionError)
try to import a module that does not exist (ImportError) and so on.
"""
# raise allows you to throw an exception at any time.
# assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
# In the try clause, all statements are executed until an exception is encountered.
# except is used to catch and handle the exception(s) that are encountered in the try clause.
# else lets you code sections that should run only when no exceptions are encountered in the try clause.
# finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.

# try and except
print("--#try and except")
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")

print()

print("--multiple exceptions --")
try:
    a = 5
    b = '0'
    print(a+b)

except TypeError:
    print('TypeError Occurred')
except:
    print('Some error occurred.')  # except: before other blocks

print("Out of try except blocks")
print()

# else and finally
print("--# else and finally")
try:
    c, d = 10, 0
    z = c/d
except ZeroDivisionError:
    print("Cannot devide by zero. Try again")
    print("Division by 0 not accepted")
except:
    print('Some error occurred.')
else:
    print("Division = ", z)
finally:
    print("Executing finally block")
    c = 0
    d = 0
print("Out of try, except, else and finally blocks.")
print()

# raise
print("# raise")
try:
    e, f = 100, 2
    r = e/2
    if r > 10:
        raise ValueError(r)
except ValueError:
    print(r, "is out of allowed range")
else:
    print(r, "is within the allowed range")

print()

# custom exception in python
print("# custom exception in python")
"""
1. Define a class that inherits from the Exception class or one of its subclasses:

2.Customize the custom error class by adding your own methods, 
properties, and attributes as needed:
3.Raise the custom error when the desired condition is met using the raise keyword:
4.Handle the custom error using a try-except block:

python

"""


class AgeLessThanZero(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"AgeLessThanZero: {self.message}"


try:
    age = int(input("what is your age? \n"))

    if (age < 0):
        raise AgeLessThanZero("Age can never be less than zero")

except AgeLessThanZero as e:
    print(str(e))

else:
    print(f"{age} is valid Age ")

print()

# file handling in python
# file handling is important in a web application
# Advantages of File Handling
# Versatility: File handling in Python allows you to perform a wide range of operations, such as creating, reading, writing, appending, renaming, and deleting files.
# Flexibility: File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files, etc.), and to perform different operations on files (e.g. read, write, append, etc.).
# User–friendly: Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
# Cross-platform: Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.

print("--# Open() functoin and read() function--")
"""

there are four different modes for opening a file...
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""
# Close Files
# It is a good practice to always close the file when you are done with it.


def open_file():
    try:
        file = open("nsereko_kayongo_julius.txt", "r")
        print(file.read())
    except FileNotFoundError as e:
        print(e)
    finally:
        file.close()


# open_file()
open_file()

print()

# Write to an Existing File or create a new file
# To write to an existing file, you must add a parameter to the open() function:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content


def writting_to_afile(filename):
    try:
        file = open(filename, "a")
        file.write("This is a new line")
    except FileNotFoundError as e:
        print(e)
    finally:
        file.close()


writting_to_afile("nsereko_kayongo_julius.txt")
print()

print("--# Delete a File--")
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
# Check if file exists, then delete it:


def delete_file(filename):
    import os
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")


delete_file("Exercise.txt")
