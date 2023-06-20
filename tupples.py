#tupples

phones = ("samsung", "toto", "iphone", "blackberry")
print (phones)

#tupples can hold any data type
phones = ("samsung", "toto", "iphone", "blackberry")
print (phones)

models = (2023,2022, 2021, 2020, 2019, 2018)

#acess tupples of models
print (models[0])
print  (models[3])




#Add items to tupple
p = list(phones)
p.append("nokia")

print (tuple(p))

#add two tuples together

laptops = ("Dell", "Microsoft", "Hp")
laptop = ("samsung",)
new_laptops = laptops + laptops
laptops +=laptop

print (new_laptops)
print (laptops)
print (laptop)

#using a for loop to iterate through a tuple
laptops = ("Dell", "Microsoft", "Hp")
for item in laptops:
    print (laptop)



