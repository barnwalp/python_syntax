from data_structure.heap_functions import build_max_heap, max_heapify


def heap_sort(input_data):
    print(build_max_heap(input_data))
    heapsize = len(input_data) - 1

    # create an empty list of size 'heapsize'
    output_data = [None] * (heapsize+1)
    # print(output_data)
    for index in reversed(range(0, heapsize+1)):
        output_data.insert(index, input_data[0])
        # since there is no replace function in python list,
        # remove none value from the list
        output_data.pop(index+1)
        # print(index)
        # print(output_data)
        input_data[0] = input_data[index]
        input_data.pop()
        max_heapify(input_data, 0)
    return output_data


input_data = [8, 9, 3, 2, 4, 10, 5]
# print(input_data)
print(heap_sort(input_data))
