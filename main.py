import os
import shutil

#directory = os.path.join(os.path.expanduser("~"), "Downloads")
directory = input("Enter the directory path: ")

extensions = {
    ".png": "Images",
    ".jpg": "Images",
    ".jfif": "Images",
    ".mp4": "Videos",
    ".pdf": "PDF Documents",
    ".exe": "Applications",
    ".msi": "Applications",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".docx": "Documents",
    ".txt": "Documents",
    ".stl": "3D print files",
    ".iso": "Disc images",
    ".mdf": "Disc images",
    ".mds": "Disc images",
    ".bin": "Disc images",
    ".dxf": "CAD drawings",
    ".dwg": "CAD drawings",
}
other_folder_name = "Other"
extension_folders = set(extensions.values())


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    elif os.path.isdir(file_path):
        if filename not in extension_folders:
            other_folder_path = os.path.join(directory, other_folder_name)
            os.makedirs(other_folder_path, exist_ok=True)

            destination_path = os.path.join(other_folder_path, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved directory {filename} to {other_folder_name} folder.")
        else:
            print(f"Skipped directory {filename}. It matches an extensions folder.")
    else:
        print(f"Skipped {filename}. Not a file or directory.")