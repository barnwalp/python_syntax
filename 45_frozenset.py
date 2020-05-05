"""
frozenset is an immutable version of set object. it can be used as key in
a dictionary. syntax of frozenset
"""

# creating a frozenset; if no iterable is pass as arguments, an empty
# frozenset will be created
my_list = [8, 9, 6, 2, 1, 5, 8, 6]
fset = frozenset(my_list)
print(fset)

x = ('a', 'b', 'c')
y = ('d', 'e', 'f')
z = ('g', 'e', 'i')


list_2 = [x, y, z]

li = []
for (_, e, _) in list_2:
    li.append((e))
print(set(li))

# or

s = set([e for (_, e, _) in list_2])
