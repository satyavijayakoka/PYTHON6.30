# program 1
# a = 100
# b = 200
# c = 0
# print(a/b)
# print(a/c) #this is an exception -- ZeroDivisionError: division by zero
# print("Hello World")

# program 2
# name = 'Mansi'
# print(name)
# print(name[0])
# print(name[2])
# print(name[7]) #IndexError: string index out of range

# program 3
# a = 100
# b = 'one'
# print(a+b) # TypeError

# program 4
# a=100
# try:
#     b = 0
#     c = a/b
#     print(c)
# except:
#     print("some error occured!!")
# print("hello world")

# # program 5
# name = 'Mansi'
# try:
#     print(name[0])
# except:
#     print("something went wrong")

# # program 6
# name = 'Mansi'
# try:
#     print(name[6]) # this will give exception
# except:
#     print("something went wrong")

# program 7 : no exceptions
# a = 10
# name = 'Mansi'
# try:
#     b=2
#     c= a/b
#     print(c)
#     print(name[2])
# except:
#     print("some error occured!!")

# program 8 :Zero div exceptions
# a = 10
# name = 'Mansi'
# try:
#     b=0
#     c= a/b
#     print(c)
#     print(name[2])
# except:
#     print("some error occured!!")

# program 9 :INdex  exceptions
# a = 10
# name = 'Mansi'
# try:
#     b=10
#     c= a/b
#     print(c)
#     print(name[7])
# except:
#     print("some error occured!!")

# # program 10
# a = 10
# name = 'Mansi'
# try:
#     b=10
#     c= a/b
#     print(c)
#     print(name[7])
# except Exception as e:
#     print("some error occured!!",e)  # some error occured!! string index out of range

# program 11
# a = 10
# name = 'Mansi'
# try:
#     b=10
#     c= a/b
#     print(c)
#     print(name[1])
# except Exception as e:
#     print("some error occured!!",e) 
# print("hello world")

# # program 12
# a = 10
# name = 'Mansi'
# try:
#     b=10
#     c= a/b
#     print(c)
#     print(name[10])
# except Exception as e:
#     print("some error occured!!",e) 
# except Exception as f:
#     print("something went wrong!!",f)
# print("hello world!!")

# # program 13
# a = 10
# name = 'Mansi'
# try:
#     b=0
#     c= a/b
#     print(c)
#     print(name[1])
# except ZeroDivisionError as e:
#     print("some error occured!!",e) 
# except IndexError as f:
#     print("something went wrong!!",f)
# print("hello world!!")


# program 13
# a = 100
# name = 'Mansi'
# try:
#     b=100
#     c= a/b
#     print(c)
#     print(name[1])
# except ZeroDivisionError as e:
#     print("some error occured!!",e) 
# except IndexError as f:
#     print("something went wrong!!",f)
# else:
#     print("code executed successfully!!") #this will be executed when there is no exception

# print("hello world!!")

#program 14
# a = 100
# name = 'Mansi'
# try:
#     b=100
#     c= a/b
#     print(c)
#     print(name[1])
# except ZeroDivisionError as e:
#     print("some error occured!!",e) 
# except IndexError as f:
#     print("something went wrong!!",f)
# else:
#     print("code executed successfully!!") #this will be executed when there is no exception
# finally:
#     print("this will always executed, irrespective of the code status")   
# print("hello world!!")


# program 15
a = 100
name = 'Mansi'
try:
    b=100
    c= a/b
    print(c)
    print(name[10])
except ZeroDivisionError as e:
    print("some error occured!!",e) 
except IndexError as f:
    print("something went wrong!!",f)
else:
    print("code executed successfully!!") #this will be executed when there is no exception
finally:
    print("this will always executed, irrespective of the code status")   
print("hello world!!")






