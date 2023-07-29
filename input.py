# input() is used to take user data

name = input("what is your name")
print("your name has ",len(name))

#variables are used to store data
#swapping
a = input("a:")
b = input("b:")

temp = a
a = b
b = temp

print("a:", a)
print("b:", b)

#greetings progam
city_name = input("what is the name of the city where you grew up ? \n")
pet_name = input("what is the name of your pet ? \n")
band_name = city_name + pet_name
print("your band name is" , band_name)
