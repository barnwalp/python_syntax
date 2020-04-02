import heapq

# heapq function on a list
input_data = [5, 7, 9, 1, 3]

# heapify the given list
heapq.heapify(input_data)

print("the created heap is: " +str(input_data))

# pushing an element in the heap
heapq.heappush(input_data, 4)

print("heap after pushing 4: " +str(input_data))

# popping smallest element from the heap
print(str(heapq.heappop(input_data)) + " is the popped item from the list")
print(input_data)

# using push and pop: this will first push the item
# then pop the smallest item from the list
print("the popped item using pushpop is: " +str(heapq.heappushpop(input_data, 1)))
print("list after adding 10 using pushpop is: " + str(input_data))

# heapreplace with first pop the smalles item and then
# push the provided items
print(str(heapq.heapreplace(input_data, 1)))
print(input_data)

print("--------------------------")

# heapq function on a tuple
tuple_data = [
    (5, [0, 5, 9]),
    (3, [4, 6]),
    (7, [10]),
    (8, [2, 3 ,11])
]

heapq.heapify(tuple_data)
print(tuple_data)

a, b = heapq.heappop(tuple_data)
print(a)
print(b)


heapq.heappush(tuple_data, (4, [7]))
print(tuple_data)



