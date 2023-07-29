# 1
names = ["Alex", "Nserweko", "Caroline", "Dave", "Eleanor"]
print(names[1])

# 2
names[1] = "julis"

# 3
names.append("Adam")
# 4
names.insert(2, "Bathel")
# 5
names.pop(3)
# 6
print(names[-1])
# 7
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
print(years[2:5])
# 8
east_africa = ["uganda", "kenya", "Rwanda", "burundi"]
east_african_comunity = east_africa.copy()
print(east_african_comunity)
# 9
for item in east_african_comunity:
    print(item)

# 10
animals = ["goat", "dog", "cat", "cow", "sheep"]
# sort in descending order
animals.sort(reverse=True)
print(animals)

# sort in ascending order
animals.sort()
print(animals)

# 11
for animal in animals:
    if "a" in animal:
        print(animal)
