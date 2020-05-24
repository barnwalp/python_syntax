def add7(x):
    return x+7


def isOdd(x):
    return x % 2 != 0


a = [1, 2, 4, 5, 6, 7, 8, 9, 10]

# filter takes the same arguments as the map function, a funtion and an
# iterable

# It will filter the list a based on the isOdd function, if isOdd returns
# true, value of a will be saved to b
b = list(filter(isOdd, a))

# This will basically save the return values of isOdd function for values
# of a
c = list(map(isOdd, a))

print(f'{b} --> {c}')

d = list(map(add7, b))
print(d)
