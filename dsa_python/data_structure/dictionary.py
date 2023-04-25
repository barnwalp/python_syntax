monthConversions = {
    0: "January",
    1: "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
d = dict()
d['a'] = 5
d['b'] = 2
print(d)
print(monthConversions)
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("not a key"))
print(monthConversions.get("others", "Not a valid key"))

# finding the minimum value as a tuple in a dictionary
dict_1 = {
    1: 8,
    2: 9,
    3: 2
}

minimum = min(dict_1.items(), key=lambda x: x[1])
print(minimum)

# The in operator uses different algorithm for lists and dictionary.
# for lists, it uses a linera search algorithm while for dictionary,
# python uses hash table which takes same amount of time no matter
# how many items are in a dictionary.

# in operator in dictionary searches for keys in the dictionary
if 1 in dict_1:
    print(dict_1.get(1))

# values can also be serched in dictionary in following way:
values = list(dict_1.values())
if 9 in values:
    print("number found")

# Dictionary as a set of counters; histogram
word = "Kriti Sanon"
d = dict()
for c in word:
    if c in d:
        # increment the counter by 1 if character is already in the dict
        d[c] = d[c] + 1
    else:
        # make a new entry if character is not in the dict
        d[c] = 1
print(d)

# Above implementation can be made more succint using .get method
word_2 = 'Ananya Mathur'
d_2 = dict()
for c in word_2:
    d_2[c] = d_2.get(c, 0) + 1
print(d_2)

# Sorting a dictionary based on keys
sorted_keys = list(d_2.keys())
sorted_keys.sort()
sorted_dict = dict()
for key in sorted_keys:
    print(key, d_2[key])
    sorted_dict[key] = d_2[key]
print(sorted_dict)
