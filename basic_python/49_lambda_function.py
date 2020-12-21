# lambda stands for anonymous function
def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85


# it can be implemented as lambda function
# func2 = lambda x: x+6
# print(func2(9))
# func3 = lamda x,y: x+y


print(func(9))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = list(map(lambda x: x+5, a))
print(newList)
