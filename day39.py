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










