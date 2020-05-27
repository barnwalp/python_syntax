
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

# aliasing
a = [1, 4, 6]
b = a

b[0] = 7
# If a refers to an object, and you assign b=a, then both variables refers
# to the same object; it's called aliasing. it is safer to avoid aliasing
# while working with mutable object
print(a)

# when a list variable is passed as a parameter to a function, then both
# variable and the function parameter work as an alias and changing one will
# automatically change the other


def delete_value(t):
    del t[0]


numbers = [2, 4, 6, 3, 1]
delete_value(numbers)
print(numbers)

# there are operators that modify the list while other that creates a
# new list. eg. append modifies the list while + create a new list


def bad_delete_head(t):
    t = t[1:]


# the slice operator will create a new list and assignment will make t refers
# to it; but none of it will have any effect on the list that was passed as
# an argument
