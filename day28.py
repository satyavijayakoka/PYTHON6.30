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












