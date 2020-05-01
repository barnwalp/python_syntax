# split method - converts string to list

user_info = 'pankaj 29'.split()
print(user_info)

name, age = 'pankaj 29'.split()
print(f'{name} --> {age}')

# join method - converts list to string
client_info = ['Prashasti', '26']

# in the inverted comma, use character with which items
# need to be joined
print(' - '.join(client_info))
