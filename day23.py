# class Person:

#     # fields and properties
#     first_name = "satya"
#     last_name = "koka"
# # instance method
#     def walk(self):
#         print("i am walking")

#     def talk(self):
#         print("i am talking")
# satya = Person()
# print(satya.first_name)
# print(satya.last_name)
# satya.walk()
# satya.talk()

# koshika = Person()
# print(koshika.first_name)
# print(koshika.last_name)
# koshika.walk()
# koshika.talk()

# koshika.first_name = "koshika"
# koshika.last_name = "koka"
# print(koshika.first_name)
# print(koshika.last_name)

# program 2
class PersonB:
    #constructor
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
    
    def talk(self):
        print("i am talking")
    
    def walk(self):
        print("i am walking")

jathin = PersonB("jathin","koka")
shiva = PersonB("shiva","koka")

print(jathin.first_name)
print(shiva.last_name)

print(shiva.first_name)
print(shiva.last_name)
shiva.city = "vijayawada"
print(shiva.city)

#Assignment
# Vehicle 
# type model
# start() , stop()
class Vehicle:
    def __init__(self,typ,mdl):
        self.type = typ
        self.model = mdl
def start(self):
    print("vehicle started")

def stop(self):
    print("vehicle stopped")

car = Vehicle("Honda","CRV")
print(car.type)
print(car.model)
















