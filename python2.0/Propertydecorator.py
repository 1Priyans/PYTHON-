class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonous = 500
    #totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonous # it's propery decorator is also known as Getter.

    @totalSalary.setter 
    def totalSalary(self, val):
        self.salaryBonous = val - self.salary # It is called as Setter method. 
 
e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salaryBonous)