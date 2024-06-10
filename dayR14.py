# program 1
# setA = {11,22,33}
# # setA.add(44)
# # print(setA)

# # setA.clear()
# # print(setA)   # set()

# setB = setA.copy()  # it will create different memory
# print(setB)


# setA = {11,22,33,44}
# setA.pop()
# print(setA)

# setA.remove(22)
# print(setA)

# # program 2
# setA = {11,22,33}
# setB = {44,55,66}
# setC = setA.union(setB)
# print(setC)

# setM = {11,22,33}
# setN = {11,44,55}
# setP = setM.intersection(setN)
# print(setP)

# program 3
setA1 = {66,56,77}
setA2 = {55,68,77}
# setA3 = setA1.difference(setA2)
# print(setA3)

# setA4 = setA2.difference(setA1)
# print(setA4)

# program - 4
# setA1.difference_update(setA2)
# print(setA1)

# program 5
# setA5 = setA1.intersection(setA2)
# print(setA5)

# setA1.intersection_update(setA2)
# print(setA1)

# setA6 = setA1.symmetric_difference(setA2)
# print(setA6)  #  {66, 68, 55, 56}

# setA1.symmetric_difference_update(setA2)
# print(setA1)

# program 6
setA = {11,22,33}
setB = {11,22}
e = setB.issubset(setA)
f = setA.issuperset(setB)
print(e)
print(f)

setN = {11,22,33,44}
setM = {11,223,335,446}  
g = setM.isdisjoint(setN)
print(g)
