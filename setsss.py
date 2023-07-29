beverages = {"cocacola", "oner", "fanta", "mirinda"}
two_more = {"ufresh", "stoney"}
beverages.update(two_more)
print(beverages)

# 3
myset = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in myset)

# 4
myset.remove("kettle")
# 5
for item in myset:
    print(item)
# 6
cars = {"prado", "gwagon", "benz", "bmw"}
car_list = ["wish", "vitz"]
cars.update(car_list)
print(cars)

# 7
fnames = {"nsereko", "julius"}
age = {21, 22}
fnames.update(age)
print(fnames)
