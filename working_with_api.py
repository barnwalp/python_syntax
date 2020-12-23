import requests


response = requests.get('https://randomfox.ca/floof')

# will return 200 if everything goes OK
print(response.status_code)

# will return the response text
# print(response.text)

# will return data in a dictionary format
print(response.json())

fox = response.json()

print(fox['image'])
