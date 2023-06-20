#list are used to store different items
fruits = ["mango", "apple", "orange", "watermellon", "pineapple"]
#print(fruits)

#duplicates 
fruits = ["mango", "mango","apple", "orange", "watermellon", "pineapple", "pineapple"]
print(fruits)

#list length
fruits = ["mango", "apple", "orange", "watermellon", "pineapple"]
print(len(fruits))

#type checking
print(type(fruits))

#acessing elements
fruits = ["mango", "apple", "orange", "watermellon", "pineapple"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

#acessin items in  a range
fruits = ["mango", "apple", "orange", "watermellon", "pineapple"]
print(fruits[0:3])
print(fruits[:3])
print(fruits[3:])
print(fruits[:])

#Adding items usind append
fruits.append("pea")
print(fruits)

#Adding items usind insert
fruits.insert(0, "banana")
print(fruits)

#removing items
fruits.remove("banana")
print(fruits)

#removing items using an index
fruits.pop(3)
print(fruits)

