#tupples

phones = ("samsung", "toto", "iphone", "blackberry")                            
print (phones)              #('samsung', 'toto', 'iphone', 'blackberry')

#tupples can hold any data type
phones = ("samsung", "toto", "iphone", "blackberry")
print (phones)              #('samsung', 'toto', 'iphone', 'blackberry')

models = (2023,2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015)

#data type
print(type(models))         #<class 'tuple'>

#length
print(len(models))          #9

#acess tupples of models
#using index
print (models[0])           #2023
print  (models[3])          #2020

#using negative indexing
print (models[-1])          #2015
print (models[-3])          #2017

#by slicing
print (models[1:5])         #(2022, 2021, 2020, 2019)
print (models[6:])          #(2017, 2016, 2015)
print(models[:-7])          #(2023, 2022)
print(models[:])            #(2023,2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015)


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
    print (item)



