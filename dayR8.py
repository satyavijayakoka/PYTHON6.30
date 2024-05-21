firstName = "chinmay"
lastName = "deshpande"
info = """
    my name is chinmay and i am learning js
"""
info2 = '''
   my name is chinmay and i am learning python
'''

# string stores the value by index
city = "pune"
print(city[0])

# update
# city[1] = "c"
# string doesnot support item assignment

fruit = "apple"
print("a" in fruit)
print("A" in fruit)

for x in range(len(fruit)):
    print(fruit[x])

for x in fruit:
    print(x)

i1 = 0
while(i1<len(fruit)):
    print(fruit[i1])
    i1 = i1 + 1

# len()
country = "india"
e = len(country)
print(e)

# upper
fruit = "apple"
q1 = fruit.upper()
print(q1)

# lower
veg = "Brinjal"
q2 = veg.lower()
print(q2)

# capitalize()
first_name = "chinmay"
q3 = first_name.capitalize()
print(q3)

# startswith
last_name = "Deshpande"
q4 = last_name.startswith("D")
q5 =last_name.startswith("De")
print(q4)
print(q5)

# endswith
city = "bangalore"
q6 = city.endswith("e")
q7 = city.endswith("re")
print(q6)
print(q7)

# replace
info = "i am learning js"
q8 = info.replace("js","python")
print(q8)

# join
info =["satya","koka","9666477714"]
q9 = '@'.join(info)
print(q9)





