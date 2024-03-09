# program 1
setA = {1,2,3}
setB = {11,22,33}
setC = setA.union(setB)
print(setC)  # {1, 2, 3, 33, 22, 11}

# program 2
setD = {11,22,33}
setE = {33,44,55}
# setF = setD.intersection(setE)
# print(setF)    #{33}

# setD.intersection_update(setE)
# print(setD) #{33}
# print(setE) #{33, 44, 55}

setE.intersection_update(setD)
print(setD)  # {33, 11, 22}
print(setE)   #{33}

# program 3
setP = {11,22,33}
setQ = {45,66,77,33}
setR = setP.symmetric_difference(setQ)
print(setR) # {66, 11, 45, 77, 22} ; 33 is removed

setP.symmetric_difference_update(setQ)
print(setQ) #{33, 66, 45, 77}
print(setP) #{66, 11, 45, 77, 22}

# program 4
setP = {11,22,33}
setQ = {45,66,77,33}
# setW = setP.difference(setQ)
# print(setW) #{11, 22}
# setP.difference_update(setQ)
# print(setP)

setQ.difference_update(setP)
print(setQ) #{66, 45, 77}

# program 5
setT = {11,22,33}
setU = {11,22,33,44}
q = setT.issubset(setU)
q2 = setU.issuperset(setT)
print(q) #True
print(q2) #True

setX = {11,22,33,44,88}
setY = {55,66,77,88}
e = setX.isdisjoint(setY)
print(e) # false

# program 6

setW = {11,22,33,44}
setW.add(55)
print(setW) #{33, 11, 44, 22, 55}

# setW.clear()
# print(setW)  # set()

# setW.pop()
# setW.remove(44)
# print(setW) # pop()--{11, 44, 22, 55}   # remove()--{11, 22, 55}

setW.update({5,6,7,8,3})
print(setW) #{33, 3, 5, 6, 7, 8, 11, 44, 22, 55}

r = setW.discard(5)
print(setW) #{33, 3, 6, 7, 8, 11, 44, 22, 55}


