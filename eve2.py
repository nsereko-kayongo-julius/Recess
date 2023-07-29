x = ("samsung", "iphone", "techno", "redmi")
print(x[-1])

# 2
print(x[-2])

# 3
y = list(x)
y[1] = ["itel"]
print(tuple(y))
# 4
y.append("huawei")
print(tuple(y))

# 5
for item in x:
    print(item)

# 6
y.pop(0)
print(tuple(y))

# 7
cities = tuple(["kampala", "nairobi", "kigali", "dodoma"])
print(cities)

# 8
(green, yellow, red, white) = cities
print(green)
print(yellow)
print(red)

# 9
print(cities[1:4])

# 10
fname = ("nsereko", )
lname = ("julius", )
names = fname + lname
print(names)

# 11
fruits = ("apples", "mango", "orange", "cabage")
multiply_tuple = fruits * 3
print(multiply_tuple)

# 12
thistuple = (1, 2, 3, 7, 8, 7, 5, 6, 8, 5)
print(thistuple.count(8))
