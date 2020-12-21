li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    # returning x to the power x
    return x**x


newList = []
for x in li:
    newList.append(func(x))

print(newList)

# using map function above line can be reduced to one line
# map function takes a function and a list as a arguments
print(list(map(func, li)))

# or it can also be used as
print([func(x) for x in li if x % 2 == 0])
