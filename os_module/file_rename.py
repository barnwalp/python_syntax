import os
import sys


path = sys.argv[1]
# path = "F:/test/"
for file_name in os.listdir(path):
    src = path + file_name
    dst = ""
    count = 0
    for char in file_name:
        if char == ".":
            break
        else:
            dst += char
            count += 1
    dst += "_"
    dst += file_name[count+1:]
    dst = path + dst
    # print(f'{src} --> {dst}')
    os.rename(src, dst)
