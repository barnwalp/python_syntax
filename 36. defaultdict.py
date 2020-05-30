from collections import defaultdict

# using list as default_factory
list_data = defaultdict(list)

list_data['python'].append("awesome")
list_data['other'].append("not relevant")
list_data['python'].append("language")
print('check')
print(f'list data is: {list_data}')
for index in list_data.items():
    print(index)

# using int as default_factory
print("-------------------")
int_data = defaultdict(int)

figure = [1, 2, 3, 4, 2, 4, 1, 2]
for index in figure:
    int_data[index] += 1
print(int_data)

# defaultdict will create any item that you
# try to access
print("-------------------")
word = "Pankaj Barnwal"
word_dict = defaultdict(int)
for char in word:
    word_dict[char] += 1

print(word_dict)
