x=10
print(x)

first_name="satya"
print(type(first_name))

last_name="koka"
print(type(last_name))

middle_name="""

vijaya

"""
print(type(middle_name))

info='''

i am learning
javascript

'''
print(type(info))
print(info)

# program 2
city ="pune"
# 0  1  2  3
# p  u  n  e
print(city[0])
print(city[1])
#print(city[5]) IndexError: string index out of range

# program 3 slicing
city2="vijayawada"
#  0   1   2   3   4   5   6   7   8    9
#  v   i   j   a   y   a   w   a   d    a
#-10  -9  -8  -7  -6  -5  -4  -3  -2   -1
# string(startindex,endindex(not included),stepsize)
e=city2[4::]
print(e)   #yawada
e2=city2[-7::]
print(e2) #ayawada
e3=city2[1:7:]
print(e3) #ijayaw
e4=city2[1:-2:]
print(e4)  #ijayawa
e5=city2[-7:-2:]
print(e5)  #ayawa
e6=city2[-7:9:]
print(e6)  #ayawad
e7=city2[0:9:3]
print(e7)  #vaw
e8=city2[::-1]
print(e8) # it wil print in reverse --> adawayajiv
e9=city2[-1:-4]
print(e9) # it wii give blank string as we cannot give before index

# program 4
city3="nagpur"
e10=city3.upper()
print(e10)

city4="PUne"
e11=city4.lower()
print(e11)

e12=city2.count('a')
print(e12) #4
