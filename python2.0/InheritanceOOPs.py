
class Employee: #Base class 
    company = "Google"  

    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee): #Derived or Child class
     Language = "Python"

     def getlanguage(self):
         print(f"This language is {self.language}")

     #def showDetails(self):
     #    print("This is not an Employee")    
e = Employee()
p = Programmer()
e.showDetails()
#This is called single inheritance
