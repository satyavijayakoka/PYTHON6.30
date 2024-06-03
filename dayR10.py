# names = ["chinmay","samay","vedant","mithilesh"]
# print(type(names))
# names2 = names
# names2[0] = "ram"
# print(names)
# print(names2)

x = 10 
print(x) # 10
y = x
print(y) # 10
y = 900
print(y) # 900
print(x) # 10


# program 2
#          0  1  2  3  4
numbers = [11,22,33,44,55]
print(numbers[0])
numbers2 = numbers
numbers2[0] = 111
print(numbers)
print(numbers2)

names = ["chinmay","shirish","samay"]
names2 = names.copy()
# names   # names2
names2[0] ="poorva"
print(names)
print(names2)


dict = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}

# dict2 = dict 
# dict2['firstName'] = "poorva"
# print(dict2)
# print(dict)

# dict3 = dict.copy()
# dict3['firstName'] = "ravi"
# print(dict3)
# print(dict)
# function 

names = ["chinmay","ram","rahul"]

def addElement(lst):
    #lst = names
    lst.append("sham")
    return lst 
a = addElement(names)
print(a)
print(names)