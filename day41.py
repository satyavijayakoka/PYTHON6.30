# program 1
import re 
str = "anil akhil annant an ak arun arati arundhati abhijit ankur"
e = re.findall(r'\ba[nk][\w]*\b',str)
print(e)

# program 2
#dd-mm-yy
str2 = 'chinmay 7-11-1989 ,amol 19-08-1990 mayuri 21-2-1990 poorva 29-10-93 shivani 27 april 1994'
e = re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str2)
d = re.findall(r'\d{2}-\d{2}-\d{4}',str2)
print(e)
print(d)

# program 3
str3 = "Hello world"
e = re.search(r'^he',str3)
if e:
    print("str3 starts with He")
else:
    print("str3 does not starts with He")

str3 = "Hello world... i am from India"
e = re.search(r'dia$',str3)
if e:
    print("ends with dia")
else:
    print("does not ends with dia")


# program 4
str4 = "Hello WoRlD"
e = re.search(r'world$',str4,re.IGNORECASE)
if e:
    print("ends with world")
else:
    print("does not ends with world")

# program5
str5 = "Rahul got 95 marks, Vijay got 89 marks Chinmay got 70 marks"
f = re.findall(r'\d{1,2}',str5)
print(f)

g= re.findall(r'[A-Z][a-z]*',str5)
print(g)

# program 6
str6 = "The meeting will start at either 9am or 9pm else at evening 6pm"
h = re.findall(r'\d{1}[a-z]*',str6)
print(h)

# search - firstOccurence
# match - start of string 
# findall - all occurences







