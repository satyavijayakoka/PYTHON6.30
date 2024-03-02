# program 1
# upper()
first_name= "satya"
print(len(first_name))
e =first_name.upper()
print(e)

#lower()
last_name = "Koka"
e2= last_name.lower() #koka
print(e2)

middle_name = "VIJAYA"
e3= middle_name.isupper()
print(e3)

e4= e2.islower()
print(e4)

# program 2
city = "pune"
e5 = city.startswith("pu")
e6= city.startswith("p")
e7 = city.startswith("P")
print(e5)
print(e6)
print(e7)

e8= city.endswith('e')
e9=city.endswith('une')
print(e8)
print(e9)

city2 ="chandrapur"
print(city2.count('r')) #2
print(type(city2.count('r'))) #<class 'int'>

# program 3

city3 = " wardha"
print(len(city3)) # 7
e10 = city3.lstrip() # removes left hand side space
print(e10)
print(len(e10)) #6

city4 = " wardha "
print(len(city4)) #8
e11 = city4.rstrip() # removes right hand side space
print(e11)
print(len(e11)) #7

city5 = " wardha "
print(len(city5)) #8
e12 = city5.strip() # removes left &right hand side space
print(e12)
print(len(e12)) #6

# program 4
info = "I am learning javascript"
e13 = info.replace("javascript","python")
print(e13) # I am learning python
print(info) # I am learning javascript


# program 5
e14 = "123".isdigit()    # 0 - 9
print(e14) #True

e15 = "123a"
e16 = e15.isalpha()
print(e16) #False

e17 = e15.isalnum() # either alphabets or numbers
print(e17)
