from operator import itemgetter


def huffman(frequency):
    from collections import defaultdict
    from heapq import heappush, heappop, heapify

    code = defaultdict(list)

    # items in heap are tuples containing a list of letters and the
    # combined frequencies of the letters in the list
    heapify(frequency)

    # reduce the heap to a single item by combining the two items
    # with the lowest frequencies
    count = 1
    while len(frequency) > 1:
        freq0, letters0 = heappop(frequency)
        print("\n")
        for ltr in letters0:
            print("selected letter and frequency is: " + str(letters0) + ", " + str(freq0))
            # insert a '0' at index 0 of the list in dict
            code[ltr].insert(0, '0')
            print("encoded dictionary is: " + str(code))
        freq1, letters1 = heappop(frequency)
        for ltr in letters1:
            print("selected letter and frequency is: " + str(letters1) + ", " + str(freq1))
            # insert a '1' at index 0 of the list in dict
            code[ltr].insert(0, '1')
            print("encoded dictionary is: " + str(code))
        heappush(frequency, (freq0 + freq1, letters0 + letters1))
        print("\nheap after " + str(count) + " iteration is: " + str(frequency) + "\n")
        count += 1

    # join all the content of the dictionary
    for k, v in code.items():
        code[k] = ''.join(code[k])
    return code


# # finding frequency of a given sentence
# input_data = "i love python"

# # create a empty dictionary
# freq = {}
#
# for char in input_data:
#     freq[char] = input_data.count(char)
#
# # converting dictionary into list of tuples
# frequency = [(x, y) for (y, x) in freq.items()]

# providing frequency tuple for the function
frequency = [
    (50, 'a'),
    (30, 'b'),
    (10, 'c'),
    (5, 'd')
]
print(frequency)
frequency = sorted(frequency, key=itemgetter(0))
print("Initial heap is: " + str(frequency))

print(huffman(frequency))
