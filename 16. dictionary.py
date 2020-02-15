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
