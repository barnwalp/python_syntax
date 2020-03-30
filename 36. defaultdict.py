from collections import defaultdict

# using list as default_factory
list_data = defaultdict(list)

list_data['python'].append("awesome")
list_data['other'].append("not relevant")
list_data['python'].append("language")

print(list_data)
for index in list_data.items():
    print(index)