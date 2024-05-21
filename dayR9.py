
#           0     1    2  3
info = ["satya","koka",40,12]

# retrive 
print(info[0])
# update
info[0]= 'koshika'
# add 
info.append('vijayawada')
# delete
info.pop()
info.pop(2)
info.remove("koka")
# available ?
print("satya" in info)

# dict 
# dictionary does not stores the value by index

info = {
    "firstName":"satya",
    "lastName":"koka",
    "age":40,
    "rollNo":12
}
#print(info[0])

# retrive 
e = info['firstName']
print(e)

# update 
info['firstName'] = "jathin"
print(info)

# add
info['age'] = 5
print(info)
info['city'] = "vijayawada"
print(info)

# delete prop
info.pop('age')
print(info)

# delete complete dictionary
#del info
#print(info)
# len
e = len(info)
print(e)
print("city2" in info)


vehicle = {
    "color":"red",
    "type":"sedane"
}

print(vehicle['color'])
# update
vehicle['color'] = "green"
print(vehicle)

#add
vehicle['regNo'] = 123
print(vehicle)

#{'color': 'green', 'type': 'sedane', 'regNo': 123}
vehicle.pop('type')
print(vehicle)

# property available or not
#{'color': 'green', 'regNo': 123}
print('Color' in vehicle)

# how many properties
print(len(vehicle))

del vehicle