
friends = ["Kevin", "Karen", "jim", "Oscar", "Toby"]

print(friends[0])

# to access items from the back of the list
print(friends[-1])

print(friends[1:])
print(friends[1:3])

friends[1] = "Mike"
print(friends[1])

# list concatenation
list_1 = [1, 4, 5]
list_2 = [1, 3, 9]

print(list_1 + list_2)

# Repeating list a serveral times
list_3 = [0, 4] * 6
print(list_3)

# list functions

# appending a list to a list using function
list_2.extend(list_1)
print(list_2)

# Deleting element
value = list_2.pop()
print(list_2)

# getting value at index 1 and deleting the same
value = list_2.pop(1)
print(list_2)

# In case deleted value is not needed, del can be used
del list_2[3]
print(list_2)

# In case index is not known, item can be deleted through value
list_2.remove(1)
print(list_2)

# Deleting more than one element
del list_3[2:5]
print(list_3)
