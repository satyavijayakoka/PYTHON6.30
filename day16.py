# program A
strA = "amol"
print(strA)
print(type(strA))

names = ["chinmay","sarika","rohit"]
print(names)
print(type(names))

info = {
    "firstName":"satya",
    "lastName":"koka"
}
print(info)
print(type(info))

# program B
flowers = ["lilly","lotus","jasmine"]
flowerB = ("lilly","lotus","rose")
flowers[0]= "rose"
print(flowers)
#flowerB[1] = "sunflower" #TypeError: 'tuple' object does not support item assignment

# program C
# does tuples store the value by index?--- yes
# how to define tuple
tupleA=("A","B","C")
print(tupleA)
print(type(tupleA))
print(tupleA[1])

# for loop with range
for x in range(len(tupleA)):
    print(tupleA[x])

# for loop without range
for item in tupleA:
    print(item)

# while loop
i1 = 0
while(i1 < len(tupleA)):
    print(tupleA[i1])
    i1=i1+1

# program D
tupleB = 12, 22
print(tupleB)
print(tupleB[0])
#tupleB[0]=34

tupleC = (11,22,33)
a,b,c = tupleC
print(a)
print(b)
print(c)

# program E
tupleD = (11,22,33)
print(len(tupleD)) # 3
e = list(tupleD)
print(e) # [11, 22, 33], converted tuple into list
e = tuple(e)
print(e)  #(11, 22, 33)

# program F
d = (11,22,33,44,44)
print(d)
print(d.count(44)) # 2

e2 = d.index(22)
print(e2) # 1
print(33 in d) # True

# how to create tuple with constructor
e3 = ([11,22,33],[33,44,55],[55,66,77])
print(e3)






