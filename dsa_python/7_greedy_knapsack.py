def greedy_knapsack(input_data, knapsack):
    # add profit/weight ratio in the input data as
    # new column
    for index in input_data:
        pw_ratio = index[0]/index[1]
        index.append(pw_ratio)

    # sorting the list based on the last column
    # of 2D array in the reverse order
    input_data.sort(key=lambda x: x[2], reverse=True)

    # sorted 2D list
    print(input_data)
    profit = 0

    for index in input_data:
        # here index[1] is weight
        if knapsack > 0 and index[1] <= knapsack:
            knapsack -= index[1]
            # here index[0] is profit
            profit += index[0]
        else:
            break
        if knapsack > 0:
            profit += index[0]*(knapsack/index[1])
    return profit


input_data = [
    [25, 18],
    [24, 15],
    [15, 10]
]
knapsack = 20
print(greedy_knapsack(input_data, knapsack))
