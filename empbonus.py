class Employee:
    def __init__(self, first, salary):
        self.first = first
        self.pay = salary

    # display employee bonus of 0.15% of salary
    def bonus(self):
        return self.pay * 0.15

    def __str__(self):
        return f"{self.first}'s salary is {self.pay}"


# creating a new employee
emp1 = Employee("Nsereko", 150000)
print(emp1.bonus())
emp2 = Employee("Julius", 230000)
print(emp2.bonus())
