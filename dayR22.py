class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln, sal):
        super().__init__(fn, ln)
        self.salary = sal
    
    def displaySalary(self):
        print(self.salary)

satya = Teacher("satya","koka",100000)
print(satya.firstName)
print(satya.lastName)
print(satya.salary)
satya.displayName()
satya.displaySalary()

# program 2
class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self, fn, ln, ffn):
        super().__init__(fn, ln)
        self.fName = ffn

    def displayFName(self):
        print(self.fName + self.lastName)

class Son(Father):
    def __init__(self, fn, ln, ffn, sn):
        super().__init__(fn, ln, ffn)
        self.sName = sn

    def displaySName(self):
        print(self.sName + self.lastName)
        super().displayFName()
        super().displayGName()

jathin = Son("Ratnam","koka","Shiva","Jathin")
print(jathin.firstName)
print(jathin.lastName)
print(jathin.fName)
print(jathin.sName)

jathin.displaySName()
        
 # program 3
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

shiva = Son("lakshmi","koka","shiva")
satya = Daughter("lakshmi","koka","satya")
print(shiva.firstName)
print(shiva.lastName)
shiva.displayMName()
shiva.displaySName()
        
print(satya.firstName)
print(satya.lastName)
satya.displayDName()
satya.displayMName()
        
# program 4
class Mother:
    def __init__(self,fn,ln):
        print("Mother constructor is called")
        self.fname = fn
        self.lname = ln

class Father:
    def __init__(self,fn,ln):
        print("Father constructor is called")
        self.fname = fn
        self.lname = ln

class Son(Father,Mother):  # leftside(father)is there so it is called
    def __init__(self, fn, ln, sn):
        super().__init__(fn, ln)
        self.sname = sn

    def displaySName(self):
        print(self.sname + self.lname)

jathin = Son("Shiva","Koka","Jathin")
print(jathin.fname)
print(jathin.lname)
jathin.displaySName()




        
        

























        




























