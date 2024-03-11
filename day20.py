def addA(x,y):
    return x+y
p = addA(22,3)
print(p)

# program 1
# lambda function
add = lambda x,y:x+y
q = add(232,2)
print(q)

# program 2
r = lambda x:x*x
print(r(12))

# program 3
def addition(x,y):
    return x+y
print(addition(122,8))

# program 4
# function as parameter to another function
add = lambda x,y:x+y
def addition(fn,x,y):
   f = fn(x,y)   # fn = lambda x,y:x+y = add
   return f
e2 = addition(add,28,3)
print(e2)  # 31

# program 5
sub = lambda x,y:x-y
def substraction(fn,s,t):
    g = fn(s,t)  # fn = lambda x,y:x-y = sub
    return g
e3 = substraction(sub,86,9)
print(e3)  # 77

# program 6
# function as a return type
# def add():
#     return lambda x,y:x+y
# e4 = add()
# print(e4)
# e5 = e4(22,4)
# print(e5)

# program 7
def add():
    return lambda x,y:[x+y,x-y,x*y,x/y]
e6 = add()
e7 = e6(22,2)
print(e7) # [24, 20, 44, 11.0]