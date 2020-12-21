import os


path = 'F:/test/'
print(len(path))
for file in os.listdir(path):
    if file.startswith('images_'):
        dst = path + file[7:]
        file = path + file
        print(f'{file} --> {dst}')
        os.rename(file, dst)
