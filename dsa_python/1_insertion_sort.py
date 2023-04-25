def insertion_sort(input_data):
    for index_j in range(len(input_data)):
        key = input_data[index_j]
        index_i = index_j - 1
        while index_i >= 0 and input_data[index_i] > key:
            input_data[index_i + 1] = input_data[index_i]
            index_i -= 1
            input_data[index_i + 1] = key
    return input_data


input_data = [2, 5, 9, 8, 6, 3, 7, 5, 1, 0]
print(insertion_sort(input_data))
