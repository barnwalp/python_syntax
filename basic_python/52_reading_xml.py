import os
from xml.etree import ElementTree as ET


# getting the XML DOM
tree = ET.parse('test.xml')

# getting the root of the tree
root = tree.getroot()

# getting the string version of the root
# print(ET.tostring(root))

# getting all the book tags
books = tree.findall('book')
authors = tree.findall('book/author')

# getting all the author name
for authors in tree.findall('book/author'):
    print(authors.text)
