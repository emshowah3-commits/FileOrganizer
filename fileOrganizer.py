import os
import shutil
import collections
from pprint import pprint

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extention = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

file_mappings = collections.defaultdict()
for filename in os.listdir(path):
    file_type = filename.split('.')[-1]
    file_mappings.setdefault(file_type, []).append(filename)
pprint(file_mappings)
print(f"moved: {filename}")