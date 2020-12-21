import os
from pathlib import Path


path = "F:/test/"
# for file in os.listdir(path):
#     print(file)

# print('-----------------')
# print(os.path)
# print('-----------------')

# os.walk will recursively travers all files in all current and sub-directory
# root is the path of the directory that is being traversesd
# dir is the directory that are in the current directory that program is in
# files are all the files that are in the current directory
for root, dir, files in os.walk(path):
    # print(f'{root} --> {dir} --> {files}\n')
    for file in files:
        if file.endswith('.png'):
            print('------------------')
            print(os.path.join(root, file))


# listing files and directory using scandir
path_2 = "/home/pankaj"

for items in os.scandir(path_2):
    # st_mtime provides the time the content of the file was last modified
    print(f'{items.name}--------------->{items.stat().st_mtime}')
    # print(items.stat().st_mtime)

nl = '\n'
print(f'{nl}-----------------------------{nl}')

# listing files and directory using pathlib.Path
# pathlib.Path have an .itemdir() method for creating an iterator of all
# files and folders in a directory. each entry yielded by the .itemdir
# contains information about the file or directory such as name and other
# attributes.

entries = Path(path_2)
for entry in entries.iterdir():
    print(entry.name)
