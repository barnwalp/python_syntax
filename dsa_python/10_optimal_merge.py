from heapq import heappush, heappop, heapify


def merge(first_list, second_list):
    # both of these will be used for for loop at the end
    index_start = 0
    index_end = len(first_list) + len(second_list)

    # append infinity at the end of first list
    first_list.append(float("inf"))

    # append infinity at the end of second list
    second_list.append(float("inf"))

    temp_index_i = 0
    temp_index_j = 0
    output_data = []
    for value in range(index_start, index_end):
        if first_list[temp_index_i] < second_list[temp_index_j]:
            output_data.insert(value, first_list[temp_index_i])
            temp_index_i += 1
        else:
            output_data.insert(value, second_list[temp_index_j])
            temp_index_j += 1
    return output_data


def optimal_merge(first_list, second_list, third_list, forth_list):
    no_of_list = 4

    # create a tuple based on the size of the list and the list
    heap = [
        (len(first_list), first_list),
        (len(second_list), second_list),
        (len(third_list), third_list),
        (len(forth_list), forth_list)
    ]
    heapify(heap)
    print("heapified lists are: " + str(heap))

    while no_of_list > 1:
        size1, list_array1 = heappop(heap)
        size2, list_array2 = heappop(heap)
        list_array3 = merge(list_array1, list_array2)
        heappush(heap, (len(list_array3), list_array3))
        no_of_list -= 1
    size, final_list = heappop(heap)
    return final_list


# sorted input arrays which needs to be merged
first_list = [2, 3, 5, 8, 9]
second_list = [5, 9]
third_list = [6, 9, 12]
forth_list = [10]

print("Final merged list is: " + str(optimal_merge(first_list, second_list, third_list, forth_list)))
