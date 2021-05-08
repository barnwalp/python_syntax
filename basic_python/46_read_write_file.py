"""
6 access mode for file IO:
1. Read only('r'): Handle is at the begining of the file.
2. Read and write('r+'): Handle is at the begining of the file.
3. Write only('w'):open the file and overwrite. file is created if it does not exist
4. Append only('a'): Handle is at the end of the file.
5. Append and Read('a+'): Handle is at the end. file is created if does not exist.
6. Write and Read('w+'): file is overwritten. 
"""

# Creating a file
with open('new.txt', 'w') as f:
    content = 'This is some random text\nmore random stuff'
    f.write(content)

# Reading a file
with open('new.txt', 'r') as f:
    for line in f.readlines():
        print(line)
