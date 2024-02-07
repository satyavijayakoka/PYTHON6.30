print("hello")
a=10
print(a)
a=100
print(a)
# Arithmetic operations

q=4
r=2
print(q+r)
print(q-r)
print(q*r)
print(q/r)
print(q%r)

s=9
t=3
print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)

def calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)

calculator(3,2)
calculator(8,2)

# function without parameter and without return type
def addA():
    print(3+3)
addA()
addA()

# function with parameter and without return type
def addB(x,y):
    print(x+y)
addB(12,4)
addB(16,4)

# function with parameter and with return type
def addC(x,y):
    return x+y
q1=addC(9,3)
print(q1)
print(q1+q1)
print(q1*q1)
print(q1*0.10)
