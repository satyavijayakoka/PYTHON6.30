# deleting record from the file

import os
reclen = 20
size = os.path.getsize('cities2.bin')
totalRecords = int(size/reclen)

f1 = open('cities2.bin','rb')
f2 = open('cities.bin','wb')

cityToBeDeleted = input('enter the city to be deleted ')
cityToBeDeleted =cityToBeDeleted + (reclen - len(cityToBeDeleted))* " "
cityToBeDeleted = cityToBeDeleted.encode()

for x in range(totalRecords):
    str = f1.read(reclen)
    if(cityToBeDeleted != str):
        f2.write(str)

f1.close()
f2.close()
os.remove('cities2.bin')
os.rename('cities.bin','cities2.bin')






















