# program 1
listA=[11,22,33]
# listB=listA
# listB[0]=55
# print(listA)
# print(listB)

# copy()
listD=listA.copy()
listD[1]=111
print(listD) #[11, 111, 33]
print(listA) #[11, 22, 33]

# extend()
listA=[11,22,33]
listA.extend([55,66,77]) # [11, 22, 33, 55, 66, 77]
print(listA)
q1 =listA.index(66)
print(q1) # 4

# program 2
birthYear=[1989,1990,1991,1992]
ages=[]
for x in birthYear:
    #print(2024-x)
    ages.append(2024-x)
print(ages)

# program 3
marks=[1,33,45,77,66,44,65,33]
above50=[]
for x in marks:
    if x>50:
        above50.append(x)
print(above50)

# program 4
numbers=[11,22,33]
total=0
for x in numbers:
    total=total+x
    #         0    +  11  -----> 11
    #         11   +   22 -----> 33
    #         33   +   33  -----> 66
print(total)

# program 5
cities=["pune","nagpur","mumbai","bangalore","chennai"]
for x in cities:
    print("welcome " + x)




