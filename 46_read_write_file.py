file = open('test.txt', 'r')

f = file.readlines()

newList = []
for line in f:
    # this if-else statement can  be replaced by using
    # newList.append(line.strip())
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
print(newList)

file_2 = open('file.txt', 'w')

for item in newList:
    file_2.write(item + '\n')

file.close()
