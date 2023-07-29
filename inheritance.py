from tkinter import messagebox
import tkinter as tk
import math
from abc import ABC, abstractclassmethod
print("---# inhertance")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking... woof woof")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")


# create Animal objects
animal = Animal(" Generic animal")

dog = Dog("Alphs")
cat = Cat("flower")
print()

# invoke eat method
animal.eat()
dog.eat()
dog.bark()
print()
cat.eat()
cat.meow()
print()

# exaple 2 demostrating inheritance


class Vechicle:
    def __init__(self, name, brand, color):

        self.name = name
        self.brand = brand
        self.color = color

        # create a method

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")

    def move(self):
        print(f"{self.name} is moving")


class Car(Vechicle):
    def __init__(self, name, brand, color, num_wheels):
        super().__init__(name, brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.num_wheels}")

    def honk(self):
        print(f"{self.name} is honking")


# create car object
my_car = Car("Ford", "Ford", "red", 4)

my_car.display_info()
my_car.move()
my_car.honk()

print()
# changing car object values
my_car.name = "landcruiser"
my_car.brand = "Toyota"
my_car.color = "blue"
my_car.num_wheels = 2
my_car.display_info()

print()

print("--# class excercise")


class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, name, length, breadth):
        super().__init__(name)
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)


circle = Circle("Circle", 5)
print("Area of circle:", circle.calculate_area())
print("Perimeter of circle:", circle.calculate_perimeter())

print()

rectangle = Rectangle("Rectangle", 10, 5)
print("Area of rectangle:", rectangle.calculate_area())
print("Perimeter of rectangle:", rectangle.calculate_perimeter())

print()
print("--# multiple inheritance--")


# example 3 multiple inheritance


class Flyable:

    def fly(self):
        print(f"{self.name} is flying")


class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Bird(animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def fly(self):
        print(f"{self.name} is flying")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"species: {self.species}")

    # create a bird object


my_bird = Bird("pigeon", "Bird")
my_bird.display_info()
my_bird.eat()
my_bird.fly()

# method overiding


class Animal:
    def make_sound(self):
        print(f"Animal makes a sound")


class Cat(Animal):
    def make_sound(self):
        print("cat is meowing")


class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")


def make_animal_sound(animal):
    animal.make_sound()


# create objects
animal = Animal()
dog = Dog()
cat = Cat()

print()

# calling make animal sound
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

print("---# polymorphism")
# Method overloading
# method overloading

# method overriding


class Shape:
    # create methods

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

# sub class rectangle


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# sub class Circle


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


# create objects
rectangle = Rectangle(10, 20)
circle = Circle(10)

# calculate Area
print(f"Area of a rectangle is {rectangle.calculate_area()}")
print(f"Area of a Circleis {circle.calculate_area()}")
print()
# calculate Perimeter
print(f"Perimeter of a rectangle is {rectangle.calculate_perimeter()}")
print(f"Perimeter of a Circle is {circle.calculate_perimeter()}")

print("---#Abstraction")


class Vechicle(ABC):
    @abstractclassmethod
    def start(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass


class Car(Vechicle):
    def start(self):
        print("starting car")

    def stop(self):
        print("stoping car")


class Truck(Vechicle):
    def start(self):
        print("starting truck")

    def stop(self):
        print("stoping truck")


# create objects
car = Car()
truck = Truck()

car.start()
truck.start()
print()
# start thr vechicle
car.stop()
truck.stop()


print("-----#Ex2 demostrate abstraction")


class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# creating objects
rectangle = Rectangle(10, 20)
circle = Circle(10)

# invoke the methods
print(f"Area of a rectangle: {rectangle.area()}")
print(f"perimeter of a rectangle: {rectangle.perimeter()}")
print()
print(f"Area of a circle: {circle.area()}")
print(f"Area of a circle: {circle.perimeter()}")

# Assignment for the reciept gui


class ReceiptPrinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Nsereko julius Restaurant Receipt Printer")
        self.root.geometry("370x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#F5F5F5")

        # Create labels and entry fields
        self.label_name = tk.Label(
            root, text="Customer Name:", font="arial 10 bold", bg="#F5F5F5")
        self.label_name.place(x=10, y=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.place(x=140, y=10)

        self.label_items = tk.Label(
            root, text="Items:", font="arial 10 bold", bg="#F5F5F5")
        self.label_items.place(x=10, y=30)
        self.entry_items = tk.Entry(root)
        self.entry_items.place(x=140, y=30)

        self.label_total = tk.Label(

            root, text="Total Amount:", font="arial 10 bold", bg="#F5F5F5")
        self.label_total.place(x=10, y=50)
        self.entry_total = tk.Entry(root)
        self.entry_total.place(x=140, y=50)

        # Create print button
        self.print_button = tk.Button(
            root, text="Print Receipt", command=self.print_receipt, bg="green", fg="white")
        self.print_button.place(x=140, y=100)

        # Create exit button
        self.exit_button = tk.Button(
            root, text="Exit", command=self.exit_program)
        self.exit_button.place(x=240, y=100)

        # Create receipt frame
        self.receipt_frame = tk.Frame(root, bg="white", padx=10, pady=10)
        self.receipt_frame.place(x=40, y=200)

    def print_receipt(self):
        heading = '---------RECIEPT----------'
        name = self.entry_name.get()
        items = self.entry_items.get()
        total = self.entry_total.get()

        if name and items and total:
            receipt = f"{heading}\nCustomer Name: {name}\n\nItems: {items}\n\nTotal Amount: {total}\n\nNote:\nonce goods are sold are not returnable"

            # Clear previous receipt if any
            for widget in self.receipt_frame.winfo_children():
                widget.destroy()

            # Display receipt in the frame
            receipt_label = tk.Label(
                self.receipt_frame, text=receipt, justify="left", bg="white")
            receipt_label.pack(anchor="w")
        else:
            self.show_error("Error", "Please fill in all fields.")

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def exit_program(self):
        self.root.quit()


# Create the main window
root = tk.Tk()

# Create an instance of the ReceiptPrinter class
receipt_printer = ReceiptPrinter(root)

# Run the application
root.mainloop()
