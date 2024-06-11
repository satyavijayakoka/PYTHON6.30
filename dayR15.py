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

# =============== june 11th =======================================

# def add(x,y):
#     return x+y
# print(add(12,4))

# lambda function

add = lambda a,b:a+b
e = add(1,4)
print(e)

sqr = lambda x: x*x
r = sqr(9)
print(r)

# program 2
# function as parameter to another function

add = lambda a,b:a+b
def addition(fn,a,b):
   # fn = lambda a,b:a+b
   e = fn(a,b)
   return e
r = addition(add,12,4)
print(r)

def substraction(fn,x,y):
    # fn = lambda x,y:x-y
    return fn(x,y)

s = substraction(lambda x,y:x-y,22,4)
print(s)


# function as return type
def greet():
    return lambda :"hello"
c = greet()
print(c())


# program 3
# default
def add(x=32,y=12):
    print(x+y)
add(11,11)

# positional arguments
def sub(x,y):
    return x-y
r = sub(y=17,x=23)
print(r)

# *args
def add(*args):
    print(args)
    total = 0
    for i in args:
        total = total + i
    return total
t = add(12,23,44,2,3,9,6,8,5,7,11,21,2,1,4,6)
print(t)

# **kwargs
def info(**kwargs):
    print(kwargs)
    kwargs['city']= "erie"
    return kwargs

r = info(name = "satya", age = "40", rollNo = 24)
print(r)









