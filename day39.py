# \w ---> [a--z A--Z 0--9]
# program 1
# only one occurence

import re
str = "man sun mop run"
result = re.search(r'm\w\w',str)
# print(result.group())
if result:
    print(result.group())   # man


# program 2
# gives all the occurences
str2 = "man ran sun fun map rap shape mate fate"
list2 = re.findall(r'm\w\w',str2)
print(list2)     # ['man', 'map', 'mat']

# program 3
str3 = "python is good language to learn"
q1 = re.match(r'p\w\w',str3)
# print(q1.group())
if q1:
   print(q1.group())  # pyt


# program 4
#\W ---- non alpha - numeric
str4 = "This ; is the : 'Core' python's book"
result = re.split(r'\W+',str4)
print(result)      # ['This', 'is', 'the', 'Core', 'python', 's', 'book']


# program 5
str5 = "i am learning javascriet and javascriet"
q2 = re.sub(r"javascriet","javascript",str5)
print(q2)   # i am learning javascript and javascript

# search()
# findall()
# match()
# split()
# sub()
# group()

# \w [a-z A-Z 0-9]
# \W [not [a-z A-Z 0-9]]
# \d - [0-9]
# \D - not[0-9]
# \b - blank space
# \A - match only start of string 
# \Z - match only at end 

# program 1
import re
str = 'an apple a day keeps doctor away'
#listA = re.findall(r'a[\w]*',str) #['an', 'apple', 'a', 'ay', 'away']
listA = re.findall(r'\ba[\w]*',str)
print(listA)

# program 2
import re
str = 'The meeting will be conducted on 1st and 21st of this month'
# 1st  21st

# program 3
# listB = re.findall(r'\b\d[\w]*',str)
# print(listB) #['1st', '21st']

listB = re.findall(r'\b\d[\d]*',str)
print(listB) #['1', '21']

# program 4
import re
str = "one two three four five six seven 8 9 10"
listC = re.findall(r'\b\w{5}\b',str)
print(listC) # ['three', 'seven']

listC = re.search(r'\b\w{5}\b',str)
print(listC.group()) #three

# listC = re.match(r'\b\w{5}\b',str)
# print(listC.group())

# program 5
str = "one two three four five six seven 8 9 10"
listD = re.findall(r'\b\w{4,}\b',str)
print(listD) # ['three', 'four', 'five', 'seven']


str = "one two three four five six seven 8 9 10"
listD = re.findall(r'\b\w{3,5}\b',str)
print(listD)  # ['one', 'two', 'three', 'four', 'five', 'six', 'seven']


str = "one two three four five six seven 8 9 10"
listD = re.findall(r'\b\d{1,}\b',str)
print(listD)  # ['8', '9', '10']

str = "one two three four five six seven 8 9 10"
listD = re.findall(r't[\w]*\Z',str)
print(listD) # []


str = "one two three four five six seven 8 9 10 two"
listD = re.findall(r'\At[\w]*',str)
print(listD)  # []






