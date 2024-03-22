
class Person:
    # constructor
    def __init__(self,fn,ln):
        # instance variables
        self.firstName = fn
        self.lastName = ln
    # instance method
    def displayName(self):
        print(self.firstName + self.lastName)
    # lastName update
    def updateName(self,ln):
        self.lastName = ln
satya = Person("satya","koka")
print(satya.firstName)
print(satya.lastName)
satya.displayName
satya.updateName("duggirala")
print(satya.lastName)

# program 2
class PersonB:
    country = "India"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def updateName(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    @classmethod
    def updateContry(cls,cn):
        cls.country = cn

h = PersonB("koshika","koka")
print(h.firstName) #koshika
print(h.lastName)
print(h.country)
h.country = "Bharat"
h.updateName("Koshika","Koka")
print(h.firstName) #Koshika(in capital K)
h2 = PersonB("jathin","koka")
print(h2.country) # India
PersonB.updateContry("india")
print(h.country) #Bharat
print(h2.country) #india


# program 3
# static method
# count number of objects
class PersonC:
    count = 0
    country = "Bharat"

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        PersonC.count = PersonC.count + 1
    
    def displayName(self):
        self.firstName+self.lastName
    
    @classmethod
    def updateContry(cls,cn):
        cls.country = cn
    
    @staticmethod
    def countObj():
        return PersonC.count

shiva = PersonC("shiva","koka")
madhu = PersonC("madhu","duggirala")

a = PersonC.countObj()
print(a)








