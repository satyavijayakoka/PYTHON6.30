# program 1
# single inheritance
# parent -- constructor , child -- no constructor

# class Student:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
#     def displayName(self):
#         print(self.firstName+self.lastName)
    
# satya = Student("satya","koka","12345")
# print(satya.firstName)
# print(satya.lastName)
# print(satya.adharNo)
# satya.displayName()

# class Teacher(Student):
#     salary = 100000

#     def displaySalary(self):
#         print(self.salary)
# satyaK = Teacher("satyaK","kokaK","12345")
# print(satyaK.firstName)
# print(satyaK.lastName)
# print(satyaK.adharNo)
# print(satyaK.salary)
# satyaK.displayName()
# satyaK.displaySalary()

# program 2
# single inheritance
# parent -- constructor , child --  constructor

# class Student:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo

#     def displayName(self):
#         print(self.firstName+self.lastName)

# class Teacher(Student):
#     def __init__(self,fn,ln,adharNo,salary):
#         super().__init__(fn,ln,adharNo)
#         self.salary = salary
    
#     def displaySalary(self):
#        print(self.salary)

# satya = Teacher("satya","koka",123,2345677)
# print(satya.firstName)  
# print(satya.lastName) 
# print(satya.adharNo) 
# print(satya.salary)          

# satya.displayName()
# satya.displaySalary()

# program 3
# multi level inheritance
class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo
    
    def displayName(self):
        print(self.firstName+self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,adharNo,salary):
        super().__init__(fn,ln,adharNo)
        self.salary = salary
    def displaySalary(self):
        print(self.salary)

class Professor(Teacher):
    def __init__(self,fn,ln,adharNo,salary,spec):
        super().__init__(fn,ln,adharNo,salary)
        self.special = spec
    
    def displaySpecialization(self):
        print(self.special)

chinmay = Professor("chinmay","deshpande",1234,55566678,"computerscience")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.adharNo)
print(chinmay.salary)
print(chinmay.special)

chinmay.displayName()
chinmay.displaySalary()
chinmay.displaySpecialization()



































