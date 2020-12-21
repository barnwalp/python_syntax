import math
value1 = math.inf
value2 = float("inf")

if value1 > value2:
    print("math.inf is greater")
else:
    print("float.inf is greater")
print(math.inf)
print(float("inf"))
print(type(math.inf))
print(type(float("inf")))

input_data = [3, 4, 5, 2]
input_data.append(float("inf"))
print(input_data)

if 3 > math.inf:
    print("yes")
else:
    print("no")

index = range(0, 6)
print(index)
