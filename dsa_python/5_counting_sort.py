# def counting_sort(input_data, size):
#     # create an empty list of length "range"
#     key = [0] * (size + 1)
#     # print(key)
#     for index in input_data:
#         key[index] = key[index] + 1
#     # print(key)
#     output_data = []
#     for index in range(size + 1):
#         while key[index] > 0:
#             output_data.append(index)
#             # print(output_data)
#             key[index] = key[index] - 1
#             # print(key[index])
#     return output_data


def counting_sort(input_data, size):

    # create an empty list of length "range"
    key = [0] * (size + 1)

    # create and empty output array
    output_data = [0] * len(input_data)
    print(output_data)

    # count the no of occurrence and store them in key as per the index
    for index in input_data:
        key[index] = key[index] + 1
    print(key)

    # modify the array key so that value at index n will be no of element that
    # are either smaller or equal to n
    for index in range(1, (size + 1)):
        key[index] += key[index - 1]
    print(key)

    right_index = len(input_data)-1
    print(right_index)
    for index in reversed(range(0, right_index+1)):
        output_data[(key[input_data[index]]-1)] = input_data[index]
        print("output data at index " + str(index) + " is " + str(output_data))
        key[input_data[index]] -= 1
        print("count array after iteration " + str(index) + " is " + str(key))
    return output_data


input_data = [2, 5, 3, 0, 2, 3, 0, 3]
# input_data = [2, 2, 2, 0, 5, 3, 2, 5, 1, 0, 4, 5, 4]
print("input data is " + str(input_data))
# size is the highest value data in the array
size = max(input_data)
print(size)
print(counting_sort(input_data, size))
