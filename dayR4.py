# list:- A list in Python is like a container that holds a collection of items.
# These items can be anything: number,string,other lists, or even more complex data types.
# list stores value by index

# # program 1
# #        0         1        2        3        4
# li = ["pragati","arina","rasmila","anisha","payal"]
# # curd - Create - Update - Retrive - Delete
# #retrive:
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[4])

#--------------------------
# update:

# li = ["laxmi","rita","prajani","sonika"]

# # append() ---->Adds an item to the end of the list.
# li.append('sabina')
# print(li)

# # insert() ----->Inserts an item at a given index in the list.
# li.insert(2,"ganesh")
# print(li)

# # extend() ---->Extends the list by appending multiple elements.
# # or it will combine two list in single list.
# li2 = ["rabindra","nabaraj"]
# li.extend(li2)
# print(li)

#------------------------------------------------------------
# sort() ----> Sorts the list in ascending order.
# li3 = [21,44,77,12,35,98,9,79,86,63]
# li3.sort()
# print(li3)

#------------------------------------------------------

# reserve() --->Reverses the elements of the list in place.
#li4 = ["erie","chicago","buffalo","newyork","erie"]
# li4.reverse()
# print(li4)

#-------------------------------------------------------

# count() ---->Returns the number of times a value appears in the list.

# li5 = [2,23,43,55,65,55,98,21,55,34]
# print(li5.count(55))
# print(li4.count('erie'))

#-----------------------------------------

# index() ---> Returns the index of the first occurrence of a value in the list.
# (Raises ValueError if the value is not present).

# li4 = ["erie","chicago","buffalo","newyork","erie"]
# print(li4.index('chicago')) # 1
# print(li4.index('erie')) # 0

#-------------------------------------------

# delete element:-
# pop() -----> Removes and returns the item at the specified index.

# If no index is specified, removes and returns the last item in the list.
li4 = ["erie","chicago","buffalo","newyork","erie"]
# li4.pop()
# print(li4) # removes last element

# li4.pop(2)
# print(li4) # removes the item at that specified index
# print(li4.pop(2))  # returns the remove item

#--------------------------------------------

# remove() ---->Removes the first occurrence of a value from the list.
# li4.remove('newyork')
# print(li4)

#------------------------------------------------

# clear() ----> Removes all items from the list. return empty list []
# li4.clear()
# print(li4)














