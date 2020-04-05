# tuples are immutable, you can not change
# the value of the tuples after declaration
coordinates = (4, 5)

print(coordinates[0])

# you can not do following line
# coordinates[1] = 12

long_coordinates = [(4, 5), (6, 7), (80, 34)]
print(long_coordinates[2][0])

# how to append elements in a list
tuple_data = (10, 50, 20, 9, 40, 25, 60, 30, 1, 56)
print(tuple_data)

# convert tuple to a list
list_data = list(tuple_data)
print(list_data)

# append a value in the list
list_data.append(100)
tuple_data = tuple(list_data)

print("tuple after appending 100: " + str(tuple_data))