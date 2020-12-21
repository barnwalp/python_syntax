import os

path = "/mnt/c/Users/panka/Downloads"
files_in_path = os.listdir(path)
# print(files_in_path)

xls_files = [file for file in files_in_path if file.endswith('.xls')]
print(f'No of xls files: {len(xls_files)}')

for file in xls_files:
    path_to_file = os.path.join(path, file)
    os.remove(path_to_file)
    print(f'{file} is deleted')
