print("goodbye")

# assign a string to a variable
a = "Hello World"
print(a)

# ultiline Strings
q = """
 This is a multiline string
 i have made it during the evening session. """

print(q)

# String concatenation
x = "Hello"
w = "World"
z = x + w
print(z)

# works when one want sto combine a string to a nuber
age = 21
# name = "Nserweko"

name = "my name is Nserweko and i am {} years old"

print(name.format(age))

# formatting
car_name = "Toyota"
car_model = "Prado"
credits = 1000000
print("I have a {} {} and i bought it at {} Ugx".format(
    car_name, car_model, credits))
