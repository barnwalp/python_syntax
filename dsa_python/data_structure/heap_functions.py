"""
A heap is a tree based DS that satisfies the heap invariant
(also called heap property): In max/min heap, for any give 
node C, if P is a parent node of C, then the key (the value) 
of P is greater/smaller than or equal to the key of C.
"""
import math


def max_heapify(input_data, root):
    # since the index starts from 0, a little tweaking is
    # required to get left and right child
    left_child = 2 * root + 1
    right_child = 2 * root + 2
    heapsize = len(input_data) - 1
    if left_child <= heapsize and input_data[left_child] > input_data[root]:
        largest = left_child
    else:
        largest = root
    if right_child <= heapsize and input_data[right_child] > input_data[largest]:
        largest = right_child
    if largest is not root:
        temp = input_data[root]
        input_data[root] = input_data[largest]
        input_data[largest] = temp
        max_heapify(input_data, largest)
    return input_data


def build_max_heap(input_data):
    # index 0 is also counted in heapsize, so heap having
    # 10 elements will return a heapsize of 9
    heapsize = len(input_data) - 1
    # leaf node starts from floor((heapsize-1)/2)+1 to n
    leaf_start_index = math.floor((heapsize-1)/2)+1
    # print(leaf_start_index)
    for index in reversed(range(0, leaf_start_index)):
        max_heapify(input_data, index)
    return input_data


def heap_extract_max(input_data):
    heapsize = len(input_data) - 1
    if heapsize < 0:
        print("heap underflow")
    max_value = input_data[0]
    input_data[0] = input_data[heapsize]
    heapsize -= 1
    input_data.pop()
    max_heapify(input_data, 0)
    return max_value


def heap_increase_key(input_data, index, key):
    if input_data[index] > key:
        print("value of key is smaller")
    else:
        input_data[index] = key
        # print(input_data)
        # print(input_data[math.floor((index-1)/2)])
        while index > 0 and input_data[math.floor((index-1)/2)] < input_data[index]:
            temp = input_data[math.floor((index-1)/2)]
            input_data[math.floor((index - 1) / 2)] = input_data[index]
            input_data[index] = temp
            index = math.floor((index-1)/2)
    return input_data


def heap_insert(input_data, key):
    input_data.append(float("-inf"))
    heapsize = len(input_data) - 1
    return heap_increase_key(input_data, heapsize, key)


# input_data = [4, 6, 5, 0, 8, 2, 7, 1, 3]
# input_data = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
# input_data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# root = 0
# print(max_heapify(input_data, root))
# print(build_max_heap(input_data))
# # print(heap_extract_max(input_data))
# # print(heap_increase_key(input_data, 7, 11))
# print(heap_insert(input_data, 8))
