
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
print("Basic list: " + str(friends))

# friends.extend(lucky_numbers)
friends.append("Creed")
print("list after appending Creed: " + str(friends))

friends.insert(1, "Kelly")
print("list after inserting Kelly: " + str(friends))

friends.remove("Jim")
# delete all elements in the list
# friends.clear()
print(friends)
friends.pop()
print(friends)

print(friends.index("Jim"))

print(friends.count("Jim"))

lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)