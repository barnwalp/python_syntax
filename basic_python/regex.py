import re


# printing raw string in python
#print(r'\tTab')
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

bat
cat
mat
rat

'''

sentence = 'Start a sentence and then bring it to an end'
def literal_search(search, text):
    pattern = re.compile(search)
    matches = pattern.finditer(text)
    li = []
    for match in matches:
        li.append(match)
    return li


# searching for phone number
print(literal_search(r'\d\d\d[-.]\d\d\d[-.]\d\d\d', text_to_search))

# searching for starting words
print(literal_search(r'^Start', sentence))

# searching for phone number starting with 800 and 900
print(literal_search(r'[89]00[-.]\d\d\d[-.]\d\d\d', text_to_search))

# searching for individual letter from a to z and A to Z
#print(literal_search(r'[a-zA-Z]', text_to_search))

# searching for cat mat rat but not bat
print(literal_search(r'[^b]at', text_to_search))

# matching multiple characters at once
print(literal_search(r'\d{3}[-.]\d{3}[-.]\d{4}', text_to_search))

# matching mr in the text
print(literal_search(r'Mr\.?\s[A-Z]', text_to_search))

"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""