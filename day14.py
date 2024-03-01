# program 1
first_name='satya'
last_name="koka"
middle_name="""
vijaya
"""
info='''
i am learning python
'''
print(type(info))

# program 2
#   0    1     2     3     4     5     6     7    8    9
#   c    h     a     n     d     r     a     p    u    r
#  -10  -9    -8    -7    -6    -5    -4    -3   -2   -1
city="chandrapur"
#print(city[startIndex:EndIndex(not included):stepSize])
print(city[1::])
print(city[2:7:])
print(city[-8::])
print(city[-8:-2:])
print(city[1:-1:])
print(city[0:10:2])
print(city[-1:-3:]) # returns blank string

# program 3
city2="pune"
print(city2[0])
print(city2[1])
print(city2[2])
print(city2[3])

for x in range(len(city2)):
    print(city2[x])

for x in range(len(city2)-1,-1,-1):
    print(city2[x])

# table of 5 in reverse
for x in range(50,4,-5):
    print(x)

# program 4
city3="nagpur"
for x in range(len(city3)):
    print(city3[x])

for char in city3:
    print(char)

for x in range(len(city3)-1,-1,-1):
    print(city3[x])

# program 5
print("i" in "chinmay")
print("in" in "chinmay")
print("iN" in "chinmay")

# program 6
city4="wardha"
i1=0
while(i1<len(city4)):
    print(city4[i1])
    i1=i1+1

i2=len(city4)-1
while(i2>=0):
    print(city4[i2])
    i2=i2-1
