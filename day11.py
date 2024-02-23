
# info={
#     "firstName":"satya",
#     "lastName":"koka",
#     "age":36,
#     "rollNo":24
# }
# print(type(info))

# # retrive
# print(info['firstName'])

# # update
# info['firstName']="koshika"
# print(info)

# # add
# info['city']="vijayawada"
# print(info)

# # delete
# info.pop('firstName')
# print(info)

# # in
# print("firstName" in info)

# Vehicle={
#     'color':"red",
#     'type':"sedane"
# }
# print(Vehicle)
# print(len(Vehicle))
# print("hello")
# print(Vehicle['color'])
# q1=Vehicle.get('coloa')
# print(q1) 
# print("bye")

Vehicle={
    'color':"red",
    'type':"sedane"
}
# Vehicle.clear()
# print(Vehicle) #{}
# de Vehicle
# print(Vehicle) # gives error as it is already deleted


animals={
    "legs":4,
    "color":"brown"
}
animals.update({"cityFound":"nagpur"})
print(animals)

info2={
    "firstName":"satya",
    "lastName":"koka",
    "age":36,
    "rollNo":24
}

for key in info2.keys():
    print(key)

for val in info2.values():
    print(val)

for k,v in info2.items():
    print(k,v)

# forloop
print(info2['firstName'])
for x in info2:
    print(x,info2[x])