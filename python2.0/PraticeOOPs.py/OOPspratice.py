class Employee:
    def __init__(self, fname, lname, salary): #Cunstructor
        self.fname = fname()
        self.lname = lname()
        self.salary = salary()

Narito = Employee("Narito", "jackson", 44000)
King = Employee("King", "khan", 44000)

print(King.name)
        