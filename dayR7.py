# string index starts with 0
# program 1
first_name = "koshika"
# 0  1  2   3   4   5    6
# k  o  s   h   i   k    a
print(first_name[0])
print(first_name[3])

# program 2
# for loop using range
city = "vijayawada"
for x in range(len(city)):
    #print(x)
    print(city[x])

city2 = "kakinada"
for x in range(len(city2)):
    print(city2[x])

#program 3
# for loop without range
city3 = "hyderabad"
for c in city3:
    print(c)

city4 = "nellore"
for c in city4:
    print(c)

# program 4
# while loop
city5 = "bangalore"
i1 =0
while(i1 <len(city5)):
    print(city5[i1])
    i1 = i1 + 1

city6 = "chennai"
i2 = 0
while(i2 < len(city6)):
    print(city6[i2])
    i2 = i2 + 1


# program 5
# particular character or substring available or not 
vegetables = "potato ladyfinger drumstick brinjal rawmango"
print("j" in vegetables)
print("rawmango" in vegetables)
print("Potato" in vegetables)


# program 6
city7 = "Erie"
for x in range(len(city7)):
    print(city7[x])

for char in city7:
    print(char)

i3 = 0
while(i3 < len(city7)):
    print(city7[i3])
    i3 = i3 + 1







