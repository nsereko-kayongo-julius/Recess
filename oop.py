class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


# car instance
my_car = Car("Ford", "Mustang", 1964)
print(my_car.make)
print(my_car.model)
print(my_car.year)
print(my_car.get_descriptive_name())
my_car.start_engine()
my_car.stop_engine()
print(my_car.odometer_reading)


class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")


# create a bank account
my_account = BankAccount(1000, 1234)
print(my_account.balance)

# deposit money
my_account.deposit(500)
print(my_account.balance)


# class studeent
class Student:
    def __init__(self, Regnunmber, age, year, course):
        self.Regnumber = Regnunmber
        self.age = age
        self.year = year
        self.course = course

    def display_details(self):
        print("name:", self.Regnumber)
        print("age:", self.age)
        print("year:", self.year)


# create a student
my_student = Student("julius", 20, 3, "computer science")

# display the details of the student
my_student.display_details()

# class Person


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # define a method
    def display_details(self):
        print("name:", self.name)
        print("age:", self.age)

    def display_details(self):
        print("name:", self.name)
        print("age:", self.age)
