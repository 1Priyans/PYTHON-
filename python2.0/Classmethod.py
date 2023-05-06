class Employee:
    company = "Camel" 
    salary = 100
    location = "Delhi"
#This is class attribute     
    
    #def changeSalary(self, sal):
    #   self.salary = sal

# We are changing the class attribute using self.__class__.salary = sal and this is called as dunder method bcoz of double underscore signs.
    #def changeSalary(self, sal)
    #    self.__class__,salary = sal
 
# We are using this method to change class atribute and this known as Class Mehod.
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(23332) #There is changing Instant Attribute not Class attributes  
print(e.salary)
print(Employee.salary)

# We can see that firstly printed e.salary as 100 bcoz of class  attribute.
# But bcoz of instance attribute e.salary will be 23332 printed as e.salary.
# And then Employee.salary will be 100 becoz the class attribute of Employee class salary is 100.   