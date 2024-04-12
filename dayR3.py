names = ["satya","sai","shiva","jathin","koshika"]
print(names)
print(names[0])

# for with range()
#            0     1      2       3        4
names = ["satya","sai","shiva","jathin","koshika"]
for item in range(5):
   # print(item)
   print(names[item])

# for loop
names = ["satya","sai","shiva","jathin","koshika"]
for item in names:
    print(item)

# while loop
names = ["satya","sai","shiva","jathin","koshika"]
i1 = 0
while(i1 < len(names)):
    print(names[i1])
    i1 = i1+1

# retrive
names = ["satya","sai","shiva","jathin","koshika"]
print(names[2])

# update
names = ["satya","sai","shiva","jathin","koshika"]
names[0] = "vijaya"
print(names)

# add --> append
names = ["satya","sai","shiva","jathin","koshika"]
names.append('madhu')
print(names)

# remove --> pop() => last element is removed
#pop(i) => the element at that index i is removed
#remove(name) => the element is removed by the name
names = ["satya","sai","shiva","jathin","koshika"]
#names.pop()
#names.pop(1)
names.remove('satya')
print(names)

# element present => we use "in"
names = ["satya","sai","shiva","jathin","koshika"]
print("shiva" in names)









