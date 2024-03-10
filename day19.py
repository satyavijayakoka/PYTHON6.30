# int as parameter and int as return type
def addOne(x,y):
    return x + y
e = addOne(12,3)
print(e) #15

# float as parameter and float as return type
def subTwo(x,y):
    return x - y
f = subTwo(12.3,12.1)
print(f) #0.20000000000000107

# boolean as parameter and boolean as return type
def canDrive(age,haveVehicle):
    if age>18 and haveVehicle:
        return True
    else:
        return False
g = canDrive(21,True)
print(g) #True

# string as parameter and string as return type
def greet(name):
    return "welcome "+name
j = greet("satya")
print(j) #welcome satya

# list as parameter and list as return type
names = ["satya","koshika","jathin","sai"]
def addName(lst):
    lst.append("shiva")
    return lst
k = addName(names)
print(k) #['satya', 'koshika', 'jathin', 'sai', 'shiva']

# dictionary as parameter and dictionary as return type
info = {
    "firstName":"satya",
    "lastName":"koka"
    #"city":"erie"
}
def addCity(information):
    information['city'] = "erie"
    return information
l= addCity(info)
print(l) #{'firstName': 'satya', 'lastName': 'koka', 'city': 'erie'}

# tuple as parameter and tuple as return type
numbers = (11,22,33)
def addValue(tupA):
    tupA = list(tupA) #[11,22,33]
    tupA.append(44)   #[11,22,33,44]
    tupA = tuple(tupA) #(11,22,33,44)
    return tupA
m = addValue(numbers)
print(m) #(11, 22, 33, 44)

# set as parameter and set as return type
setA = {11,22,33}
def addElement(seta):
    seta.add(44)
    return seta
n = addElement(setA)
print(n) #{33, 11, 44, 22}