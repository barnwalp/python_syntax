def partition(input_data, index_start, index_end):
    pivot = input_data[index_end]
    i = index_start - 1
    for index in range((index_start+1), (index_end+1)):
        if input_data[index] < pivot:
            i += 1
            temp = input_data[i]
            input_data[i] = input_data[index]
            input_data[index] = temp
    i += 1
    if input_data[i] > pivot:
        temp = input_data[i]
        input_data[i] = pivot
        input_data[index_end] = temp
    partition_index = i
    print(input_data)
    return partition_index


def quick_sort(input_data, index_start, index_end):
    if index_start < index_end:
        partition_index = partition(input_data, index_start, index_end)
        print("partition index is found at: " + str(partition_index) +
              " & pivot value is: " + str(input_data[partition_index]))
        print("quick sort is being called with starting index at: " +
              str(index_start) + " and ending index at: " + str(partition_index))
        quick_sort(input_data, index_start, partition_index)
        print("quick sort is being called with starting index at: " +
              str(partition_index+1) + " and ending index at: " + str(index_end))
        quick_sort(input_data, (partition_index+1), index_end)
    return input_data


input_data = [6, 7, 1, 10, 9, 12, 8]
index_start = 0
index_end = len(input_data) - 1
print(quick_sort(input_data, index_start, index_end))
