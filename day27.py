# single inheritance

class Father:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastNmae = ln
    
    def displayName(self):
        print(self.firstName + self.lastNmae)
    
class Son(Father):
    def __init__(self,fn,ln,sn):
        super().__init__(fn,ln)
        self.sName = sn
    
    def displaySName(self):
        print(self.sName + self.lastNmae)

jathin = Son("shiva","koka","jathin")
print(jathin.firstName)
print(jathin.lastNmae)
print(jathin.sName)
jathin.displayName()
jathin.displaySName()

# multi-level inheritance

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fName = ffn
        
    def displayFName(self):
        print(self.fName + self.lastName)
    
class Son(Father):
    def __init__(self,fn,ln,ffn,sn):
        super().__init__(fn,ln,ffn)
        self.sName = sn
    
    def displaySName(self):
        print(self.sName + self.lastName)

shiva = Son("venkateswarlu","koka","venkataratnam","shiva")
print(shiva.firstName)
print(shiva.lastName)
print(shiva.fName)
print(shiva.sName)

shiva.displayFName()
shiva.displayName()
shiva.displaySName()

# Hierarichal inheritance
class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def displayMName(self):
        print(self.firstName + self.lastName)

class Son(Mother):
    def __init__(self,fn,ln,sn):
        super().__init__(fn,ln)
        self.sName = sn

    def displaySName(self):
        print(self.sName + self.lastName)

class Daughter(Mother):
    def __init__(self,fn,ln,dn):
        super().__init__(fn,ln)
        self.dName = dn

    def displayDName(self):
        print(self.dName + self.lastName)

shiva = Son("Bhagyalakshmi","koka","shiva")
print(shiva.firstName)
print(shiva.lastName)
print(shiva.sName)
shiva.displayMName()
shiva.displaySName()

satya = Daughter("Bhagyalakshmi","koka","satya")
print(satya.firstName)
print(satya.lastName)
print(satya.dName)
satya.displayDName()
satya.displayMName()













