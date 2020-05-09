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

print(monthConversions["Nov"])
# or
print(monthConversions.get("Dec"))
print(monthConversions.get(1))

print(monthConversions.get("others"))

print(monthConversions.get("others", "Not a valid key"))

# finding the minimum value as a tuple in a dictionary
dict_1 = {
    1: 8,
    2: 9,
    3: 2
}

minimum = min(dict_1.items(), key=lambda x: x[1])
print(minimum)
