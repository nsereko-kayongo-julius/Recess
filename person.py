class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius*self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


# circle one
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


# rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # calculate area
    def calculate_area(self):
        return self.length * self.width

    # calculate perimeter
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# rectangle one
rectangle1 = Rectangle(10, 20)
print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())


# rectangle two
