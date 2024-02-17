# list
# program 1
#         0        1         2       3
names=["rama","lakshmana","sita","anjaneya"]
print(names)
names[2]="koushalya" # updating the value
print(names)

# program 2
# list stores the value by index
city=["pune","nagpur","bangalore","chennai","hydearbad"]
print(city[0])
print(city[2])
print(city[4])

# program 3
# number of elements in list
#          0       1        2      3        4      5
fruits=["mango","apple","orange","grape","kiwi","guava"]
print(fruits)
print(len(fruits)) # 6
print(fruits[5])

# program 4
# how to update the value in list
animal=["tiger","lion","bear","leopard","panther"]
animal[0]="jaguar"
print(animal)

# for loop
# for loop with range()
# while loop

# program 5
#           0       1         2        3         4          5
country=["India","Nepal","Srilanka","China","Bnagladesh","Pakistan"]
for x in range(len(country)):
    print(country[x])

for x in range(len(country)-1,-1,-1):
    print(country[x])

# program 6 another way of writing for loop
#       0         1         2           3
city=["pune","bangalore","kolkata","hyderabad"]
for item in city:
    print(item)

# program 7
# while loop
flowers=["lilly","jasmine","rose","sunflower"]
i1=0
while(i1<len(flowers)):
    print(flowers[i1])
    i1=i1+1

# reverse
i2=len(flowers)-1
while(i2>=0):
    print(flowers[i2])
    i2=i2-1

# program 8
#           0      1      2         3       4
vehicle=["car","bike","scooter","cycle","lorry"]
i3=0
while(i3<len(vehicle)):
    print(vehicle[i3])
    i3=i3+1

# reverse
i4=len(vehicle)-1
while(i4>=0):
    print(vehicle[i4])
    i4=i4-1

# program 9
# any element present in list
#          0      1       2        3        4
vehicle=["car","bike","scooter","cycle","lorry"]
print("scooter" in vehicle) # True
print("Car" in vehicle) # False





