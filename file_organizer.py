

import os
import shutil


folder_path = input("Enter folder path to organize: ")


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Audio': ['.mp3', '.wav']
}


if not os.path.exists(folder_path):
    print("Folder does not exist.")
    exit()


files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)

    
    if os.path.isdir(file_path):
        continue

    
    _, extension = os.path.splitext(file)
    extension = extension.lower()

    moved = False

    
    for folder_name, extensions in file_types.items():
        if extension in extensions:
            target_folder = os.path.join(folder_path, folder_name)

            
            os.makedirs(target_folder, exist_ok=True)

            
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved: {file} -> {folder_name}")

            moved = True
            break

    
    if not moved:
        other_folder = os.path.join(folder_path, 'Others')
        os.makedirs(other_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(other_folder, file))
        print(f"Moved: {file} -> Others")

print("\nFiles organized successfully!")