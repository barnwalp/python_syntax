# split method - converts string to list

user_info = 'pankaj 29'.split()
print(user_info)

name, age = 'pankaj 29'.split()
print(f'{name} --> {age}')

# join method - converts iterables such as list, tuple
# string, dictionary and set to a string
client_info = ['Prashasti', '26']

# in the inverted comma, use string with which items
# need to be joined
print(' - '.join(client_info))

# this takes format of string.join(iterable)
string_1 = 'pankaj'
string_2 = '123'
print(string_1.join(string_2))

test = {'python', 'java', 'javascript'}
s = '->->->'
print(s.join(test))
