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

# tuples are also comparable and hashable, meaning we can sort lists
# of them and use tuple as key value in dictionaries.

emp_tuple = ()
print(type(emp_tuple))

s_tuple = tuple('pankaj')
print(s_tuple)

# tuples also support slice operator.
# you cant modify the elements of a tuple, but your ca replace one
# tuple with another
t = ('B', ) + s_tuple[:]
print(t)

txt = 'but soft what light in yonder window breaks'
words = txt.split()
word_list = list()

for word in words:
    word_list.append((len(word), word))

word_list.sort(reverse=True)
print(word_list)

sorted_txt = list()
for length, word in word_list:
    sorted_txt.append(word)

print(sorted_txt)

# Tuple assignment, here right side can be any kind of sequence(string, list
# or tuple)
x, y = sorted_txt[:2]
print(f'{x} --> {y}')
print((x, y))
(k, l) = sorted_txt[:2]
print((k, l))

# Swapping variables using tuples
x, y = y, x
print(f'{x} --> {y}')

# Dictionaries have a method called items that returns a list of tuples where
# each tuple is key-value pair:

dict_1 = {'a': 10, 'b': 1, 'c': 22}

# following line will return a list of tuples
list_of_tuples = list(dict_1.items())
print(list_of_tuples)
for char, number in dict_1.items():
    print(f'{char} ==> {number}')
