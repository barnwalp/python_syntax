import requests
import os


r = requests.get('https://xkcd.com/353/')
# print(r)

# This will list out all the attributes and methods of repsonse obeject
print(dir(r))

# This will provide manual style document for request object
print(help(r))
print(r.text)

image = requests.get('https://imgs.xkcd.com/comics/python.png')
print(image.content)

path = 'C:/Users/panka/Desktop/comic.png'
# saving the image as comic.png
with open('comic.png', 'wb') as f:
    f.write(image.content)

print(image.status_code)

# Check if request to the site is ok or not
print(image.ok)
print(image.headers)

payload = {'page': 2, 'count': 25}

# will return https://httpbin.org/get?page=2&count=25
r = requests.get('httpbin.org/get', params=payload)
print(r.url)

payload = {'username': 'panka', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

