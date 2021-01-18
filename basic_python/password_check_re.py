import re


li = list()
for _ in range(int(input())):
    li.append(input())

for word in li:
    alphanumeric_check = 0
    no_of_digit = 0
    no_of_uppercase = 0
    no_of_letter = 0
    for char in word:
        no_of_letter += 1
        if re.match('[A-Za-z0-9]', char):
            if re.match('\d', char):
                no_of_digit += 1
            elif re.match('[A-Z]', char):
                no_of_uppercase += 1
        else:
            alphanumeric_check = 1
    char_repeat = 0
    count = {}
    for s in word:
        if s in count:
            count[s] += 1
            char_repeat += 1
        else:
            count[s] = 1
    if (alphanumeric_check == 0 and no_of_digit >= 3 and no_of_uppercase >= 3 and no_of_letter == 10 and char_repeat == 0):
        print("Valid")
    else:
        print("Invalid")

