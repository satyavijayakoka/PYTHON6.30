students =[
    {
        "firstName":"satya",
        "lastName":"koka",
        "age":40,
        "rollNo":24,
        "skills":["python","javascript","java","sql"]
    },

    {

        "firstName":"madhu",
        "lastName":"duggirala",
        "age":44,
        "rollNo":22,
        "skills":["python","html","java","sql","css"]
    },

    {

        "firstName":"sai",
        "lastName":"madireddy",
        "age":42,
        "rollNo":12,
        "skills":["python","html","java","css"]
    }


]

# program 1
for student in students:
    print(student['firstName']+ ":" +student['lastName'])

# program 2  eg:- satya:3(skills)
for student in students:
    print(student['firstName']+ ":" +str(len(student['skills'])))

# program 3
# average age of all students
total = 0
for student in students:
    total = total + student['age']
print(total/len(students))

# program 4
# add react skills to every student
for student in students:
    total = total + student['age']
print(total/len(students))

#program 5
# country : "India"
for student in students:
    student['country']:"India"
print(students)

# program 6
# names above age >=42
for student in students:
    if(student['age']>= 42):
        print(student['firstName'])



