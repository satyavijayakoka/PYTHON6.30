
# program 1
birthYear = [1989,1990,2000,2001]
ages = []
for i in birthYear:
    e = 2024 - i
    ages.append(e)
print(ages)

# list comprehension
f = [2024 - i for i in birthYear]
print(f)


# program 2
marks = [22,44,55,22,33,55,66]
above50 = []
for i in marks:
    if(i > 50):
        above50.append(i)
print(above50)

e = [i for i in marks if i > 50]
print(e)


# program 3
listE = [45,66,33,44,56]
oddEven = []
# ['odd','even','odd','even','even']
for i in listE:
    if i % 2 == 0:
        oddEven.append("even")
    else:
        oddEven.append("odd")
print(oddEven)

f = ["even" if i % 2 == 0 else "odd" for i in listE]
print(f)





















