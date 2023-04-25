def counting_sort(input_data, exponent):
    size = len(input_data)

    # The output_data array elements that will have sorted arr
    output_data = [0] * (size)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for index in range(0, size):
        value = (input_data[index] / exponent)
        count[int((value) % 10)] += 1

    # Change count[index] so that count[index] now contains actual
    # position of this digit in output_data array
    for index in range(1, 10):
        count[index] += count[index - 1]

    # Build the output_data array
    index = size - 1
    while index >= 0:
        value = (input_data[index] / exponent)
        output_data[int(count[int((value) % 10)] - 1)] = input_data[index]
        count[int((value) % 10)] -= 1
        index -= 1

    # Copying the output_data array to input_data[],
    # so that arr now contains sorted numbers
    index = 0
    for index in range(0, len(input_data)):
        input_data[index] = output_data[index]


def radix_sort(input_data):
    # Find the maximum number to know number of digits
    maximum = max(input_data)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exponent is passed. exponent is 10^i
    # where i is current digit number
    exponent = 1
    while maximum / exponent > 0:
        counting_sort(input_data, exponent)
        exponent *= 10


# Driver code to test above
input_data = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(input_data)
print(input_data)
