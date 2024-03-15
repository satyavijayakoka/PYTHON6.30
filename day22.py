# program 1
lst = [1989,1990,1991,1992]
ages = []

for i in lst:
   x =  2024-i
   ages.append(x)
print(ages)

# using map function
a = list(map(lambda x:2024-x,lst))
print(a)

# using list comprehension
print([2024-i for i in lst])

# program 2
names = ["satya","koshika","jathin","sai"]
above5 = []
for x in names:
    if len(x)>5:
        above5.append(x)
print(above5)

# using list comprehension
print([x for x in names if len(x)>5])

# using filter function
b = list(filter(lambda x: len(x)>5,names))
print(b)

# program 3
transcations = []
d = [3,4,5,-55,-77,99,33,-22,666]

for x in d:
    if x<0:
        transcations.append("withdrawl")
    else:
        transcations.append("deposit")
print(transcations)

# using list comprehension and ternary operator
print(["withdrawl" if x<0 else "deposit" for x in d])

# using filter function
print(list(filter(lambda x: x<0,d)))
print(list(filter(lambda x: x>0,d)))