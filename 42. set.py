"""
 A set is an unordered collection data type that is iterable, mutable and
 has no duplicate elements.Set has a highly optimized method for cheking
 whether a specific element is contained in the set based on hash table.
 Since sets are unordered, we can not access them using index, like list.
"""
# creating an empty set
set1 = set()

my_set = set(['a', 'b', 'c'])

print(my_set)

# Adding data in a set
my_set.add('d')
print(f'set after adding data: {my_set}')

my_set_1 = {'Richa', 'Arti', 'Archana'}

my_set_2 = {'jay', 'idri', 'Arti'}

# time complexit of union is O(len(s1) + len(s2)), s1,s2 are set
master_set = my_set_1.union(my_set_2)
print(f'union of set1 and set2 is: {master_set}')

# time complexity of intersection is O(min(len(s1), len(s2)))
my_set_3 = my_set_1.intersection(my_set_2)
print(f'intersection of set1 and set2 is: {my_set_3}')

"""
key in s	       containment check
key not in s	   non-containment check
s1 == s2	       s1 is equivalent to s2
s1 != s2	       s1 is not equivalent to s2
s1 <= s2	       s1 is subset of s2
s1 < s2	           s1 is proper subset of s2
s1 >= s2	       s1 is superset of s2
s1 > s2	           s1 is proper superset of s2
s1 | s2	           the union of s1 and s2
s1 & s2	           the intersection of s1 and s2
s1 – s2	           the set of elements in s1 but not s2
s1 ˆ s2	           the set of elements in precisely one of s1 or s2
"""
