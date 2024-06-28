# program 1

# outside the class 
# using constructor 
# using get and set method

# instance method  class level method   static method
class Person:
    # class variable 
    country = "India"

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    # instance method
    def addCity(self,cty):
        self.city = cty
    
    # instance method 2
    def updateLastName(self,ln):
        self.lastName = ln

    # class level method
    @classmethod
    def updateCountry(cls,updateCountry):
        cls.country = updateCountry

shiva = Person("shiva","koka")
madhu = Person("madhu","duggirala")
sai = Person("sai","madireddy")
print(shiva.firstName)
print(shiva.lastName)
print(shiva.country)  # India

shiva.country = "Bharat"
print(shiva.country)  # Bharat

Person.updateCountry("bharat")
print(sai.country)
print(shiva.country)


# program 2
# total number of objects

class Emp:
    Count = 0
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        Emp.Count = Emp.Count + 1

    @staticmethod
    def countObj():
        return Emp.Count
    
emp1 = Emp("satya","koka")
emp2 = Emp("sai","madireddy")
emp3 = Emp("nalini","velugoti")
e = Emp.countObj()
print(e)

















