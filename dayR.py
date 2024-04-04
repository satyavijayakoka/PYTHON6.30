# program 1
x = 10
print(x)
x = 23
print(x)

# program 2
p = 9
q = 6
print(p+q)
print(p-q)
print(p*q)
print(p/q)
print(p%q)

r = 12
s =4
print(r+s)
print(r-s)
print(r*s)
print(r/s)
print(r%s)

# program 3
def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
Calculator(4,2)
Calculator(25,5)

# program 4
# function without parameter without return type
def addA():
    print(3+3)
addA()
addA()
addA()

# function with parameter without return type
def addB(x,y):
    print(x+y)
addB(12,3)
addB(15,5)

# function with parameter with return type
def addC(x,y):
    return x+y
q1 = addC(8,4)
print(q1)
print(q1*0.10)

# program 5
l = 12
print(type(l))
m = 3.5
print(type(m))
n="satya"
print(type(n))
o = True
print(type(o))

# program 6
# comparison operators < , > , <= , >= , !=
print(2 > 4)
print(2 >= 4)
print(2 <= 4)
print(2 < 4)
print(2 == 4)
print(2 != 4)
print(2 == 2)
print(2 >= 2)
print(2 <= 2)

# program 7
# logical operators
# and 
# True    and   True  -------> True
# True    and   False  ------->False
# False    and  True  -------> False
# False    and  False  ------->False
print(2 == 2 and 4 == 4)
print(2 == 2 and 4 != 4)
print(2 != 2 and 4 == 4)
print(2 != 2 and 4 != 4)

# or
# True    or   True  -------> True
# True    or   False  ------->False
# False   or  True  -------> False
# False   or  False  ------->False
print(2 == 2 or 4 == 4)
print(2 == 2 or 4 != 4)
print(2 != 2 or 4 == 4)
print(2 != 2 or 4 != 4)

# not
#not True ----> false
#not False ----->True
print(not(2 == 2))
print(not(2 != 2))

# program 8
# conditional statements
numT = 8
if numT > 0 and numT <= 5:
    print("5% discount")
if numT > 5 and numT <= 10:
    print("10 % discount")
if numT > 10:
    print("20 % discount")

numT = -8
if numT > 0 and numT <= 5:
    print("5% discount")
elif numT > 5 and numT <= 10:
    print("10 % discount")
elif numT > 10:
    print("20 % discount")
else:
    print("incorrect input")

# program 9
# marks = 92
# if marks > 90:
#     print("Grade A")
# if marks > 75:
#     print("Grade B")
# if marks >65:
#     print("Grade C")

# program 10
marks = 92
if marks > 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("invalid please try again")

# program 11
x1 = 20
y1 = 50
if x1 > y1:
    print("x1 is greater")
else:
    print("y1 is greater")

# program 12
x1 = 100
x2 = 50
x3 = 200
if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x3 and x2 > x1:
    print("x2 is greater")
else:
    print("x3 is greater")













