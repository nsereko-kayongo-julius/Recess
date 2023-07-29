#dictionary
#A dictionary is a collection of key-value pairs. For example,
mydictionary = {
    "gwagon": "Mercedes Benz",
    "range rover": "Land Rover",
    "prado": "Toyota",
    "lambo": "Lamborghini",
    "macan": "Porsche",
}

print(mydictionary)

#length of a dictionary
print(len(mydictionary))

#data type
print(type(mydictionary))

#accessing items
z = mydictionary["gwagon"]
print(z)

y = mydictionary.get("prado")
print(y)

#Exercise1: use the values( method to return the values of the dictionary)
x = mydictionary.values()

#exercise2: to check if a key exists in a dictionary, use the in keyword
if "macan" in mydictionary:
    print("Yes, macan is one of the keys in the mydictionary dictionary")
    print(mydictionary["macan"])

#execise3:  give an example on how to changedictionary items, how to update a dictionary
mydictionary["macan"] = "Porsche Macan"
print(mydictionary)

mydictionary.update({"lambo": "Lamborghini"})
print(mydictionary)

#exercise4: to remove an item from a dictionary, use the pop() method
