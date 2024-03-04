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