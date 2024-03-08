# program 1 list
names = ["satya","koshika","jathin","shiva"]
print(names)

# program 2 dictionary
info = {
    "firstName":"satya",
    "lastName":"koka",
    "rollNo":12,
    "age":36
}
print(info)

# program 3 tuple
numbers = (11,22,33,44)
print(numbers)

# program 4 string
h = "satya"

# program 5 duplicates allowed
listA = [11,22,33,44,33,55]
print(listA)

# program 6 duplicates not allowed it enters only time "age"
info = {
    "firstName":"satya",
    "lastName":"koka",
    "age":34,
    "age":36
}
print(info)

# program 7
name = "sattya"
print(name)

# program 8 
#set
setA ={11,22,33,44}
print(type(setA))

# allow duplicate values? ans: not allowed and unordered
setB = {11,22,33,22,44,55,55}
print(setB) #{33, 22, 55, 11, 44}
print(len(setB)) # 5

# stores value by index?
# print(setB[0]) ans: no, so we can not use range for loop
for i in setB:
    print(i)

# program 9
# add()
setC = {11,22,33,44,55}
setC.add(66)
print(setC) # {33, 66, 22, 55, 11, 44}

setC.pop()
print(setC) # {66, 22, 55, 11, 44} , 33 is removed

setC.remove(11)
print(setC) # {66, 22, 55, 44} 










