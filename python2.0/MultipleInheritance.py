class Employee: #Base class 
    company = "BharatPay"  
    eCode = 120

class Freelancer:
    company = "Fiber"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Priyansh"
e = Employee()
p = Programmer()
f = Freelancer()
print(p.upgradeLevel)
print(p.level)

