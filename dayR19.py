# program 1
class Person:
    fn = "satya"
    ln = "koka"
    def displayName(self):
       print(self.fn+self.ln)
satya = Person()
sai = Person()

satya.displayName()
sai.displayName()

sai.fn = "sai"
sai.ln = "madireddy"
sai.displayName()

# program 2
# updating the value at the time of object create
class PersonB:
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln
    def displayName(self):
        print(self.fn+self.ln)

satya = PersonB("satya","koka")
satya.displayName()
sai = PersonB("sai","madireddy")
sai.displayName()

# program 3
# getter and setter method
class PersonC:
    def setFn(self,fn):
        self.fn = fn
    def getFn(self):
        return self.fn
    
    def setLn(self,ln):
        self.ln = ln

    def displayName(self):
        print(self.fn+self.ln)

sai = PersonC()
sai.setFn('sai')
sai.setLn('madireddy')
sai.displayName()

# program 4
class PersonD:
    # constructor
    country = "india"
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln
    
    # class level method
    @classmethod
    def changeCountry(cls):
        cls.country = "bharat"
    
    # instance method
    def displayName(self):
        print(self.fn+self.ln)
    
koshika = PersonD("koshika","koka")
sai = PersonD("sai","madireddy")

print(sai.country)
print(koshika.country)

sai.country = "bharat"
print(sai.country)
print(koshika.country)

PersonD.changeCountry()
print(sai.country)
print(koshika.country)















