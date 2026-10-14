import os
import shutil

source_folder = os.path.expanduser("~/Desktop/TestFolder")
target_folder = os.path.expanduser("~/Desktop/SortedFolder")

os.makedirs(source_folder, exist_ok=True)
os.makedirs(target_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved: {filename} -> {target_folder}")