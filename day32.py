# compile time error
# def add():
# print(1+3)

# run time error
# print("hello")
# e = int(input("enter the number A"))
# f = int(input("enter the number B"))
# print(e/f)
# print("bye")

# print("hello")
# numbers = [11,222,333,44,55,6,7]
# print(numbers[8])
# print("bye")

# logical error

# def calculateBonusSalary(amount):
#     #return amount + amount * 0.10
#     return amount * 0.10
# print(calculateBonusSalary(1000))

# program 2
# print("hello")
# try:
#     e = int(input("enter the number A"))
#     f = int(input("enter the number B"))
#     print(e/f)
# except Exception:
#     print("please enter correct input")
# print("bye")

# program 3
# print("hello")
# names = ["satya","jathin","koshika","sai"]
# try:
#     e = int(input("enter the number A"))
#     f = int(input("enter the number B"))
#     print(e/f)
#     print(names[9])
# except ArithmeticError:
#     print("please enter the correct input")
# except IndexError:
#     print("add more element to list")
# except Exception:
#     print("please correct the values")
# print("bye")

# program 4
# print("hello")
# try:
#     e = int(input("enter the number A"))
#     f = int(input("enter the number B"))
#     print(e/f)
# except ArithmeticError:
#     print("please enter correct input")
# finally:
#     print("i will always execute")
# print("bye")

# program 5
print("hello")
try:
    e = int(input("enter the number A"))
    f = int(input("enter the number B"))
    print(e/f)
except ArithmeticError:
    print("please enter correct input")
else:
    print("i will run")
finally:
    print("i will always execute")
print("bye")











