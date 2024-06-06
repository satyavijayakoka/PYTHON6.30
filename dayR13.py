# set
# list stores duplicate values
names = ["satya","sai","madhu","shiva","jathin","koshika","satya"]
print(names)

# set does not allow to store duplicate values
names = {"satya","sai","koshika","neelima"}
print(names)

# program 2
# list stores the value by index
names2 = ["pragati","aruna","arina","prajani"]
print(names2[1])
names2 = {"pragati","aruna","arina","prajani"}
#print(names2[2])

# program 3
for item in names2:
    print(item)

# program 4
print("aruna" in names2)

# collections ---> list, string, tuple, dictionary, set
s = "satya"
t = ("satya","sai")
l = ["shiva","neelima"]
d = {
    "firstName":"satya",
    "lastName":"koka"
}
s2 = {"satya","sai"}
print(len(s))
print(len(t))
print(len(l))
print(len(d))
print(len(s2))

listA = [11,22,33]
print(max(listA))
print(min(listA))

del s
del t
del l
del d
del s2

setA = {11,22,33}
# setB = setA
# setB.remove(22)
# print(setA)
# print(setB)


setB = setA.copy()
print(setB)
setB.remove(22)
print(setA)
print(setB)












