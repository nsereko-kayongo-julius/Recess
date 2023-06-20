#store multiple items in a single variable

#unchanged but one can reove and write
#

language_set = {"kiswahili", "luganda", "English", "lusoga",}
print(language_set)

#duplicate in sets
language_set = {"kiswahili", "luganda", "English", "lusoga", "kiswahili", "luganda", "English", "lusoga",}
print(language_set)

#data type
print(type(language_set))

#Accessing items in a set
for item in language_set:
    print(item)


#Adding items in a set
language_set = {"kiswahili", "luganda", "English", "lusoga", "kiswahili", "luganda", "English", "lusoga",}
print(language_set)
language_set.add("Swahili")
print(language_set)

#find nuber of set elements
print('total Elements: ', len(language_set))

#remove an Element from aset
language_set =  {"kiswahili", "luganda", "English", "lusoga", "kiswahili", "luganda", "English", "lusoga",}

#remove english
removed_value = language_set.discard('English') 
print('setAfter removal:', language_set )

#Adding 2 sets in python, we use a built in methtod called union 
#first set
A = {1, 3, 5}

#second set
B = {0, 2, 4}

#perform union operation using union()
numbers = A.union(B)
print(numbers)
