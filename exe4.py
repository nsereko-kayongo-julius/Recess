shoes = {
    "brand": "Nike",
    "color": "black",
    "size": 40
}
print(shoes["size"])
# 2
shoes.update({"brand": "Adidas"})
print(shoes)
# 3
shoes.update({"type": "sneakers"})

# 4
print(shoes.keys())

# 5
print(shoes.values())

# 6
print("size" in shoes)

# 7
for x, y in shoes.items():
    print(x, y)

# 8
shoes.pop("color")
print("color" in shoes)

# 9
shoes.clear()

# 10
mydetails = {
    "name": "Nsereko kayongo julius",
    "age": 21,
    "year": "year II"

}

nsereko_details = mydetails.copy()
print(nsereko_details)

# 11
# nested dictionaries
mycars = {
    "car1": {
        "name": "bmw",
        "year": 2004
    },
    "car2": {
        "name": "gwagon",
        "year": 2007
    },
    "car3": {
        "name": "prado",
        "year": 2011
    }
}

print(mycars["car1"]["name"])
