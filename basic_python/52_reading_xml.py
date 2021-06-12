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
# for authors in tree.findall('book/author'):
#     print(authors.text)

# Reading xml data from a variable
xml_data = """
    <?xml version="1.0"?>
    <catalog>
        <book id="bk101">
            <author>Gambardella, Matthew</author>
            <title>XML Developer's Guide</title>
            <genre>Computer</genre>
            <price>44.95</price>
            <publish_date>2000-10-01</publish_date>
            <description>An in-depth look at creating applications 
            with XML.</description>
        </book>
        <book id="bk102">
            <author>Ralls, Kim</author>
            <title>Midnight Rain</title>
            <genre>Fantasy</genre>
            <price>5.95</price>
            <publish_date>2000-12-16</publish_date>
            <description>A former architect battles corporate zombies, 
            an evil sorceress, and her own childhood to become queen 
            of the world.</description>
        </book>
        <book id="bk103">
            <author>Corets, Eva</author>
            <title>Maeve Ascendant</title>
            <genre>Fantasy</genre>
            <price>5.95</price>
            <publish_date>2000-11-17</publish_date>
            <description>After the collapse of a nanotechnology 
            society in England, the young survivors lay the 
            foundation for a new society.</description>
        </book>
    </catalog>
"""
print(type(xml_data))
dom = ET.fromstring(xml_data)
# for value in dom.findall('book/prices'):
#     print(value.text)
