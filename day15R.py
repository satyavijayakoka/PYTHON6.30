# program 1
# first_name = "chinmay"

# print(first_name.upper())
# print(first_name.lower())
# print(first_name.isupper())
# print(first_name.islower())

# program 2
first_name = " chinmay "
print(len(first_name))
print(len(first_name.rstrip()))
print(len(first_name.lstrip()))
print(len(first_name.strip()))

# program 3
last_name = "deshpande"
print(last_name.startswith("d"))
print(last_name.startswith("de"))
print(last_name.startswith("De"))

print(last_name.endswith("e"))
print(last_name.endswith("de"))
print(last_name.endswith("Nde"))

# program 4
marks = "123a"
print(marks.isdigit())   # ttakes  (0 to 9)
print(marks.isalpha())   # takes only alphabets
print(marks.isalnum())   # takes combination not special characters
print(type(marks))

# program 5
# full_name = " "
# e2 = full_name.isspace()
# print(e2) # true

full_name = " a"
e2 = full_name.isspace()
print(e2)  # False 

# program 6
firstN = "chinmay"
e3 =firstN.capitalize()
print(e3) # Chinmay

e4 = "I Am Learning Javascript"
print(e4.istitle())

# program 7
info = ["satya","koka","9666477714"]
e5= "@".join(info)
print(e5)

# program 8
email= "ammu.duggi123@gmail.com"
e6 = email.split('@')     # ['ammu.duggi123', 'gmail.com']
print(e6)

# program 9
# find()
emailaddress = "chinmaya"
print(emailaddress.find('a')) #5
print(emailaddress.find('a',6)) #7
#print(emailaddress.find('a',8))  # -1

# program 10
# removeprefix()
email2 = "gmail.com@chinmay"
email3 = "gmail.com@samay"
email4 = "gmail.com@sham"
print(email4.removeprefix('gmail.com@'))

# program 11
#["chinmay","samay","sham"]
students = [email2,email3,email4]
lista =[]   
for x in students:
    q1 = x.removeprefix('gmail.com@')
    lista.append(q1)
print(lista)

# program 12
# names = ["chinmay","poorva","sham","nirnay"]
students = {
    "1":"chinmayadmin",
    "2":"poorvaceo",
    "3":"shamcustomer",
    "4":"nirnaymanager"
}

roles = ["admin","ceo","customer","manager"]
names = []
for name in students.values():
    for role in roles:
        if role in name:
            q2 = name.removesuffix(role)
            names.append(q2)
print(names)

# swapcase()
a = "hello"
print(a.swapcase()) #HELLO
b = "GOod"
print(b.swapcase()) #goOD

#zfill()
name = "satya"
name2 = "vijaya"
print(name.zfill(9))
print(name2.zfill(9))