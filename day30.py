# compile tome error
# def addition(x,y):
# print(x+y)
# addition(2,3)

#run time error
# print("hello")
# x= int(input('enter the number one'))
# y= int(input('enter the number two'))
# print(x/y)
# print("bye")

# #logical error
# def add10per(amount):
#     return amount* 0.10
# e = add10per(100)
# print(e)

# program 3
print("hello")
try:
    x = int(input('enter the number A'))
    y = int(input('enter the number B'))
    print(x/y)
except Exception:
    print("invalid input")
print("bye")