# # three modes 
# # read , write , append

# program 1
# # opening the file
# f = open("myfile.txt",'w')
# #taking input from the user
# name = input('Enter the name ')
# # writing to file
# f.write(name)
# # closing the file
# f.close()

# program 2
# fileName = input('please enter the fileName ')
# f = open(fileName,'r')
# str = f.read()
# print(str)
# f.close()

# program 3
# f = None
# try:
#     fileName = input('please enter the fileName ')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print('file not found')
# finally:
#     if f is not None:
#         f.close()

# program 4
f = open('myfile2.txt','w')
while str != "@":
    str = input('enter the name'+'\n')
    if str != '@':
        f.write(str+'\n')
f.close()


















