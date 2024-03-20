# program 1
class Person:
    #constructor
    def __init__(self,fn,ln):
        self.firstName  = fn
        self.lastName = ln
    # instance method
    def display_name(self):
        print(self.firstName + self.lastName)

satya = Person("satya","koka")
sai = Person("sai","madireddy")
print(sai.firstName)
print(sai.lastName)
print(satya.firstName)
print(satya.lastName)
sai.display_name()
satya.display_name()

# program 2
class Person2:
    country = "Bharat"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)
    
    @classmethod
    def changeCountry(cls,cnty):
        cls.country = cnty

satya = Person2("satya","koka")
madhu = Person2("madhu","duggirala")
jathin = Person2("jathin","koka")

print(satya.firstName)
print(satya.lastName)
print(satya.country)
satya.displayName()

madhu.country = "India"
print(madhu.firstName)
print(madhu.lastName)
print(madhu.country)
madhu.displayName()

print(jathin.country)

Person2.changeCountry("Hindustan")
print(satya.country)
print(madhu.country)
print(jathin.country)









