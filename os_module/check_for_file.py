import os
import time


file_path = '/mnt/c/Users/panka/Downloads/Nozzle Sale Report.xlsx'
while not os.path.exists(file_path):
    time.sleep(2)

print(f'{file_path} exists')
