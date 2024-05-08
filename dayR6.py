names = ["satya","madhu","shiva","jathin"]
print(names)
print(type(names))

# retrive
print(names[1])

# update
names[0]="koshika"
print(names)

# add
names.append("sai")
print(names)

# delete --pop()
names.pop()
names.pop(1)
print(names)

# in
print('shiva' in names)
    #          0         1         2       3           4        5
country = ["India",'Bangladesh','China','Pakistan','Srilanka','Nepal']
for x in range(6):
    print(country[x])

for cntry in country:
    print(cntry)

i1 =0
while(i1<len(country)):
    print(country[i1])
    i1 = i1 +1

# methods
fruits = ["apple","banana","mango","grapes","orange"]
fruits.append("guava")
print(fruits)

fruits.pop()
fruits.pop(1)
fruits.remove('grapes')
print(fruits)

fruits.clear()
print(fruits)

numbers = [11,22,33]
numbers.clear()
print(numbers)

numbers.insert(0,199)
numbers.insert(1,99)
numbers.insert(2,999)
numbers.insert(3,9999)
numbers.insert(4,99999)
numbers.insert(2,11999)
print(numbers)

# extend
a =[11,22,33]
b= [44,55,66,22]
b.extend(a)
print(a)
print(b)
#------------------------------------------------------------------------------
# program 1
# methods
names2 = ["ram","sham","siya","ria","tia"]
print(names2)
names3 = names2
print(names3)
# i have changed the address of names2 as names3 but memory is same
names3[1]="jia"
print(names2)
print(names3)

# program 2
cities = ["vijayawada","kakinada","gudivada","vemulavada"]
citiesB = cities.copy()
# here cities and citiesB have different memory locations
citiesB[0]="Bezawada"
print(cities)
print(citiesB)

# program 3
country2 = ["JAPAN",'RUSSIA','USA','UK','POLAND']
country2.pop()
country2.pop(2)
country2.remove('UK')
print(country2)

# program 4
numbers2 = [111,222,333,444]
numbers2.append(44444)
print(numbers2)

numbers2.insert(1,2222)
print(numbers2)

# program 5
marks = [98,87,76,65,54]
marks.clear()
print(marks)

# program 6
vegetables = ["potato","tomato","brinjal","drumstick","potato","cabbage"]
v1 = vegetables.count("potato")
print(v1)

v2 = vegetables.index("brinjal")
print(v2)

vegetables.reverse()
print(vegetables)

vegetables.sort()
print(vegetables)





