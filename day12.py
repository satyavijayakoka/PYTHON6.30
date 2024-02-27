# program 1
# info3={
#     "firstName":"satya",
#     "lastName":"koka",
#     "rollNo":24,
#     "age":36
# }
# print(info3['firstName'])
# print(info3.get('firstName'))

# y=info3.setdefault('city',"hyderabad")
# print(y)
# print(info3)

# # program 2
# info4= dict.fromkeys(["keyone","keytwo","keythree"])
# print(info4)

# program 3

students=[
    {
        "firstName":"satya",
        "lastName":"koka",
        "age": 36,
        "skills":["html","css","js"]
    },
     {
        "firstName":"koshika",
        "lastName":"koka",
        "age":8 ,
        "skills":["html","css","js","python"]
    },
     {
        "firstName":"jathin",
        "lastName":"koka",
        "age": 5,
        "skills":["html","css","js"]
    }
]
# print(students[2]['firstName'])

# for x in students:
#     print(x['firstName'])

# program 4 user with python skill
for x in students:
   # print(x['skills'])
   if "python" in x['skills']:
    print(x['firstName'])

# program 5 user with python skills and age>6

for x in students:
    if x['age']> 6 and "python" in x['skills']:
        print(x['firstName'],x['age'],x['skills'])


# program 6 name and number of skills
for x in students:
    print(x['firstName']+":"+str(len(x['skills'])))

# program 7 average of all students age
total=0
for x in students:
    total=total+x['age']
print(total/len(students))

