# function :
# program 1
# int as parameter and int as return type
def add(x,y):
    return x+y
r = add(12,3)
print(r)

# program 2
# float as parameter and float as return type
def add(x,y):
    return x+y
t = add(23.5,5.9)
print(t)

# string as parameter and string as return type
def greet(name):
    return "hello "+name
e = greet("satya")
print(e)

# boolean as parameter and boolean as return type
def canDrive(above18):
    if above18:
        return True
    else:
        False
f = canDrive(True)
if(f):
    print("Allowed to drive....")
else:
    print("Not allowed to drive")

# list as parameter and list as return type
city = ["pune","mumbai","bangalore","kolkatta"]
def addCity(lst):
    lst.append("wardha")
    return lst
g = addCity(city)
print(g)

# dictionary as parameter and dictionary as return type
dict = {
    "firstName":"satya",
    "lastName":"koka"
}
def addCityToInfo(info):
    info['city'] = "pune"
    return info
h = addCityToInfo(dict)
print(h)

# tuple as parameter and tuple as return type
def addNum(tupA):
    tupA = list(tupA)
    tupA.append(555)
    tupA = tuple(tupA)
    return tupA
a,b,c = addNum((3,6))
print(a)
print(b)
print(c)

# set as parameter and set as return type
setA = {11,12,13}
def addToSetA(ss):
    ss.add(14)
    return ss
i = addToSetA(setA)
print(i)
# print(setA)































