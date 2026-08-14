''' Exercise - 7 -->  Write a program to clear the clutter inside a folder on your computer. 
                    You should use os module to rename all the png images from 1.png all the way 
                    till n.png where n is the number of png files in that folder.
                     Do the same for other file formats. 

'''


import os

# Folder path
path = r"C:\Users\professer_kartik\Desktop\garbage"

# Get all files in the folder
files = os.listdir(path)

i = 1

# Rename each file
for file in files:

    # Old file path
    old_name = os.path.join(path, file)

    # Get file extension (.jpg, .png, .txt, etc.)
    extension = os.path.splitext(file)[1]

    # New file path
    new_name = os.path.join(path, str(i) + extension)

    # Rename file
    os.rename(old_name, new_name)

    i += 1

print("All files renamed successfully!")







    