
# 2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for index_i in range(len(number_grid)):
    for index_j in range(len(number_grid[index_i])):
        print(number_grid[index_i][index_j])
    print("------")

# or

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)
