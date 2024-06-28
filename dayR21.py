class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher:
    def __init__(self,fn,ln,sal):
        self.firstName = fn
        self.lastName = ln
        self.salary = sal

    def displayName(self):
        print(self.firstName + self.lastName)

    def displaySalary(self):
        print(self.salary)

sai = Student("sai","madireddy")
print(sai.firstName)
print(sai.lastName)
sai.displayName()

###################### INHERITANCE #######################################

# program 1
# parent - constructor , child - no constructor

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    salaray = 100000

    def displaySalary(self):
        print(self.salaray)

shiva = Teacher("shiva","koka")
print(shiva.firstName)
print(shiva.lastName)
print(shiva.salaray)
shiva.displayName()
shiva.displaySalary()
    
# program 2
# single inheritance

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln,sal):
        super().__init__(fn, ln)
        self.salary = sal

    def displaySalary(self):
        print(self.salary)

satya = Teacher("satya","koka",1000000)
print(satya.firstName)
print(satya.lastName)
print(satya.salary)
satya.displayName()
satya.displaySalary()

# program 3
# multi level inheritance
class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self, fn, ln, ffn):
        super().__init__(fn, ln)
        self.FName = ffn

    def displayFName(self):
        print(self.FName + self.lastName)

class Daughter(Father):
    def __init__(self, fn, ln, ffn, dn):
        super().__init__(fn, ln, ffn)
        self.DName = dn

    def displayDName(self):
        print(self.DName + self.lastName)

koshika = Daughter("Ratnam","Koka","Shiva","Koshika")
koshika.displayDName()
koshika.displayFName()
koshika.displayName()
print(koshika.firstName)
print(koshika.lastName)
print(koshika.FName)
print(koshika.DName)
        
        
# program 4
# hierarchical inheritance
class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)

class Son(Mother):
    def __init__(self, fn, ln, sn):
        super().__init__(fn, ln)
        self.SName = sn

    def displaySName(self):
        print(self.SName + self.lastName)

class Daughter(Mother):
    def __init__(self, fn, ln, dn):
        super().__init__(fn, ln)
        self.DName = dn

    def displayDName(self):
        print(self.DName + self.lastName)

shiva = Son("Bhagyalakshmi","koka","shiva")
print(shiva.firstName)
print(shiva.lastName)
print(shiva.SName)
shiva.displayMName()
shiva.displaySName()

satya = Daughter("Bhagyalakshmi","koka","satya")
print(satya.firstName)
print(satya.lastName)
print(satya.DName)
satya.displayDName()
satya.displayMName()
        
# program 5
# multiple inheritance

class Father:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayFName(self):
        print(self.firstName + self.lastName)

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)
        
class Son(Father,Mother):
    def __init__(self, fn, ln, sn):
        super().__init__(fn, ln)
        self.SName = sn
    
    def displaySName(self):
        print(self.SName + self.lastName)

shiva = Son("Ratnam","Koka","Shiva")
print(shiva.firstName)
print(shiva.lastName)
print(shiva.SName)
shiva.displayFName()
shiva.displaySName()




















    
    





























    








































    
    
























