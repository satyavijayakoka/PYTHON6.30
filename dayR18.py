# class Person:
#     fn = "satya"
#     ln = "koka"

#     def display(self):
#         print(self.fn+self.ln)
    
# satya = Person()
# satya.display()

# sai = Person()
# sai.display()

# # sai.fn = "sai"
# # sai.ln = "madireddy"
# # sai.display()         # which is not the correct way to set values after defining the object


class Person:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def display(self):
        print(self.firstName+self.lastName)

satya = Person("satya","koka")
print(satya.firstName)
print(satya.lastName)
satya.display()

koshika = Person("koshika","koka")
print(koshika.firstName)
print(koshika.lastName)
koshika.display()













