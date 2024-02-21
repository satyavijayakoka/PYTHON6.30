#  program 1 list[]
# names=["satya","koshika","jathin","ratnam","lakshmi"]
# # retrive
# print(names[0])
# # update
# names[0]="shiva"
# print(names)
# # add
# names.append("neelima")
# print(names)
# names.insert(1,"meenakshi")
# print(names)
# # delete
# names.pop()
# print(names)
# names.pop(1)
# print(names)
# names.remove("ratnam")
# print(names)
# # in
# print("shiva" in names)
# print("Lakshmi" in names)

# program 2 dictionary{}
info=["satya","koka",35,56]
info2={
    #"key":value
    # property:value
    "firstName":'Satya',
    "lastName":'Koka',
    "age":35,
    "rollNo":56
}
# retrive
e=info2["firstName"]
print(e)

# update
info2["firstName"]="Ratnam"
print(info2)

# add
info2["city"]="vijayawada"
print(info2)

# delete
info2.pop("firstName")
print(info2)

# program 3
Vehicle={
    "color":"blue",
    "type":"honda",
    "color":"red",
}
print(type(Vehicle)) #<class 'dict'>

#length
print(len(Vehicle)) #2

#in --present or not
print("color" in Vehicle) #True

# duplicate keys
print(Vehicle)

# retrive
print(Vehicle["color"])




















