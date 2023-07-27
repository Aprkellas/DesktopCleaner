import os
import shutil
# import datetime


def main():
    desktop_path = os.path.expanduser("~\OneDrive\Desktop")
    organize_folders = {
        '.csv': os.path.join(desktop_path, "CSV Archive"),
        '.sa': os.path.join(desktop_path, "SA Archive")
    }

    #  
    for folder in organize_folders.values():
        try:
            os.makedirs(folder)
            print(f"{folder} made")
        except FileExistsError as e:
            print(f"{folder} already exists")
            print(e)
    move_files(desktop_path, organize_folders)

def move_files(source_folder, target_folders):
    # start = datetime.datetime.now()
    files = os.listdir(source_folder)  # List all files in the source folder

    for file in files:
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path) and is_csv_file(file):  # Check if it's a file (not a folder) and if it's a CSV file
            file_name = os.path.basename(file_path)

            if file_name in {"OFFICE_STATIC.csv", "OFFICE_ERS.csv", "OFFICE_STATIC.sa",  "OFFICE_ERS.sa"}:
                continue  # Skip moving "OFFICE_STATIC.csv"

            _, extension = os.path.splitext(file_name)
            if extension.lower() in target_folders:
                target_path = target_folders[extension.lower()]
                os.makedirs(target_path, exist_ok=True)
                shutil.move(file_path, os.path.join(target_path, file_name))
                print(f"Moved {file_name} to {target_path}")
    # finish = datetime.datetime.now()
    print (finish-start)

def is_csv_file(file_name):
    _, extension = os.path.splitext(file_name)
    print(extension.lower() == '.csv')
    return extension.lower() == '.csv'


if __name__ == "__main__":
    main()
