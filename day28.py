# polymorphism

# class Calculator:
#     # def addition(self,x,y):
#     #     print(x+y)
    
#     # def addition(self,x,y,z):
#     #     print(x+y+z)
    
#     # def addition(self,x,y,z,a):
#     #     print(x+y+z+a)
    
#     def addition(self, x= None, y = None, z = None, a = None):
#         if(x != None and y != None and z != None and a != None):
#             print(x+y+z+a)
#         elif(x != None and y != None and z != None):
#             print(x+y+z)
#         elif(x != None and y != None):
#             print(x+y)

# cal = Calculator()
# cal.addition(23,4)
# cal.addition(23,4,5)
# cal.addition(23,4,5,6)

# same class same method different signature

class Addition:

    def add(self,x,y):
        print(x+y)
    
    def add(self,x,y,z):
        print(x+y+z)
    
    def add(self,x,y,z,a):
        print(x+y+z+a)
    
    def add(self, x = None, y = None, z = None, a = None):
        if x != None and y != None and z != None and a != None:
            print(x+y+z+a)
        elif x != None and y != None and z != None:
            print(x+y+z)
        elif x != None and y != None:
            print(x+y)

a = Addition()
a.add(12,4)
a.add(13,4,5)
a.add(23,12,15,10)

# program 2
# class Dog:
#     def talk(self):
#         print("bow bow")

# class Human:
#     def talk(self):
#         print("Hello Hi")

# def call_talk(obj):
#     obj.talk()

# s = Human()
# t = Dog()

# call_talk(s)
# call_talk(t)

# program 3
class Dog:
    def talk(self):
        print("bow bow")

class Human:
    def talk(self):
        print("Hello Hi")

class Duck:
    def sound(self):
        print("quack quack")

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()  
   
s = Human()
t = Dog()
u = Duck()

call_talk(s)
call_talk(t)
call_talk(u)
#-------------------------------------------------
print("hello"+"bye") #hellobye
print(4+5) #9
print([1,2,3]+[11,22,33]) #[1, 2, 3, 11, 22, 33]

# class Bookx:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages + other.pages

# class Booky:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages + other.pages

# ramayan = Bookx(120)
# mahabarath = Booky(45)
# print(ramayan.pages+mahabarath.pages)
# print(ramayan+mahabarath)
# print(mahabarath+ramayan)

print(4>2) # True

# class Bookx:
#     def __init__(self,pages):
#         self.pages = pages
#     def __gt__(self,other):
#         return self.pages > other.pages

# class Booky:
#     def __init__(self,pages):
#         self.pages = pages
#     def __lt__(self,other):
#         return self.pages < other.pages

# ramayan = Bookx(120)
# mahabarath = Booky(130)
# print(ramayan.pages + mahabarath.pages) #250
# print(ramayan > mahabarath) # False
# print(mahabarath < ramayan) # False

# overriding

class WorldBank:
    def save(self):
        print("I am save from worldbank")
    def loan(self):
        print("I am loan from worldbank")

class SBI(WorldBank):
    def save(self):
        print("I am save from SBI")
        super().save()
    def loan(self):
        print("I am loan from SBI")
        super().loan()

class PNB(WorldBank):
    def save(self):
        print("I am save from PNB")
        super().save()
    def loan(self):
        print("I am loan from PNB")
        super().loan()

a = SBI()
a.save()
a.loan()
















