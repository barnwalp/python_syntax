import requests
from bs4 import BeautifulSoup as bs


# load the webpage contents
r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

# convert to a beautifulsoup object
soup = bs(r.content)

# print out the indented html page
# print(soup.prettify())

# get the first tag that it finds
first_header = soup.find('h2')
# print(first_header)

# get the list of all the h2
headers = soup.find_all('h2')
# print(headers)

# Pass in a list of elements to look for, this will print out
# the first tag that will be encountered, in this case first
# h1 tag will be returned
first_header = soup.find(['h2', 'h1'])
# print(first_header)

headers = soup.find_all(['h1', 'h2'])
print(headers)

print('---------------------------------')
print(soup.prettify())
