class Person:
    country = "india"

    def takebreath(self):
        print("i am breathing......")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        super().takeBreath()
        print(f"Salary is {self.salary}")

    def takebreath(self):
        print("I am an Employee so I am lukily breathing....")

class Programmer(Employee):
    company = "Infoysis"

    def getsalary(self):
        super().takeBreath()
        print("No salary to programmer")

p = Person()
p.takebreath()

e = Employee()
e.takebreath()

pr = Programmer()
pr.takebreath()
