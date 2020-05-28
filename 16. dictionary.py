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

# in operator in dictionary searches for keys in the dictionary
if 1 in dict_1:
    print(dict_1.get(1))

# values can also be serched in dictionary in following way:
values = list(dict_1.values())
if 9 in values:
    print("number found")
