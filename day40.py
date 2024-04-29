import re

#\w  [a-z][A-Z][0-9]
#\b  blank space
#\d  only digits

# program 1
str = "an apple a day keeps doctor away"
#e1 = re.findall(r'a[\w]*',str)
e1 = re.findall(r'\ba[\w]*',str)
print(e1)

# program 2
str2 = "The meeting will be conducted on 21st and 22nd and 1st"
e2 = re.findall(r'\d[\w]*',str2)
e3 = re.findall(r'\d[\d]*',str2)
print(e2)
print(e3)

# program 3
str3 = "one two three four five six seven 8 9 10 ad44566m"
e4 = re.findall(r'\w{5}',str3)
print(e4)
e5 = re.findall(r'\w{3,5}',str3)
e6 = re.findall(r'\w{4,}',str3)
print(e5)
print(e6)

# program 4
e7 = re.findall(r'\d{1,}',str3)
print(e7)
e8 = re.findall(r'\b\d{1,}\b',str3)
print(e8)

# program 5
str4 = 'one two three four five six seven eight nine ten'
e9 = re.findall(r't[\w]*\Z',str4)
print(e9)

e10 = re.findall(r'\Ao[\w]*',str4)
print(e10)

# program 6
str5 = "satyakoka:9666477714"
e11 = re.search(r'\d+',str5)
print(e11.group())

# program 7
str6 = "an apple a day keeps doctor away"
print(re.findall(r'a\w+',str6))
print(re.findall(r'a[\w]*',str6))








