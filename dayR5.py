# list methods
# sort
# based on value of the variable

list_num = [12,23,20,30,40,11,22,33]
print(list_num.sort()) # None: inplace changes
print(list_num)

list_alpha = ['a','b','x','s','w','e','z']
list_alpha.sort()
print(list_alpha)

# list_alnum = ['a',12,22,12,'a', 'b', 'x', 's', 'w', 'e', 'z']
# print(list_alnum)
# list_alnum.sort() # TypeError

list_alnum1 = ['a','12','22','12','a', 'b', 'x', 's', 'w', 'e', 'z']
list_alnum1.sort()
print(list_alnum1)

# reverse
# based on INdex position 
#            0  1  2  3  4  5  6  7
list_num = [12,23,20,30,40,11,22,33]
list_num.reverse()
print(list_num)

list_alnum = ['a',12,22,12,'a','b','x','s','w','e','z']
list_alnum.reverse()
print(list_alnum)






