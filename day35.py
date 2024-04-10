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
# f = open('myfile2.txt','w')
# while str != "@":
#     str = input('enter the name'+'\n')
#     if str != '@':
#         f.write(str+'\n')
# f.close()
    
# program 5
# r w
# f = open('myfile2.txt','a+')
# while str != '@':
#     str = input("enter the names ")
#     if str != '@':
#         f.write(str + '\n')
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close()

# program 6
import os , sys
# fname = input("enter the filename:  ")
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     sys.exit()
# print("the file contents are : ")
# str = f.read()
# print(str)
# f.close()

# program 7
# count --> words, characters, lines

fname = input("enter the filename: ")
if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print("file doesnot exist")
    sys.exit()

cc = 0
cw = 0
cl = 0

for line in f:
    cl = cl+1
    list = line.split()  #["satya" "learning" "AJAX"]
    cw = cw + len(list)
    cc = cc + len(line)

print(cl) 
print(cw)
print(cc)

f.close()









































