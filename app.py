import os
import shutil
# import datetime

"""
Script to clear your desktop of csv & Spatial Analyzer files
"""

def main():
    desktop_path = os.path.expanduser("~\OneDrive\Desktop")
    organize_folders = {
        '.csv': os.path.join(desktop_path, "CSV Archive"),
        '.xit64': os.path.join(desktop_path, "SA Archive")
    }

     
    for folder in organize_folders.values():
        try:
            os.makedirs(folder)
            print(f"{folder} made")
        except FileExistsError as e:
            print(f"{folder} already exists")
            print(e)

    try:
        os.makedirs("Archive")
        print("Archive made")
    except FileExistsError as e:
            print(f"{folder} already exists")
            print(e)
    archive = os.path.join(desktop_path, "Archive")

    move_files(desktop_path, organize_folders)
    move_folders(desktop_path, archive)

def move_files(source_folder, target_folders):
    # start = datetime.datetime.now()
    files = os.listdir(source_folder)  

    for file in files:
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path) and is_csv_or_sa_file(file):  
            file_name = os.path.basename(file_path)
            file_name_uppercase = file_name.upper()

            if "OFFICE_STATIC" in file_name_uppercase or "OFFICE_ERS" in file_name_uppercase:
                continue  

            _, extension = os.path.splitext(file_name)
            if extension.lower() in target_folders:
                target_path = target_folders[extension.lower()]
                os.makedirs(target_path, exist_ok=True)
                shutil.move(file_path, os.path.join(target_path, file_name))
                print(f"Moved {file_name} to {target_path}")
    
    # finish = datetime.datetime.now()
    # print (finish-start)

def is_csv_or_sa_file(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower() in {'.csv', '.xit64'}

def move_folders(source_folder, archive_folder):
    with os.scandir(source_folder) as folders:
        found_ora = {}
        found_kia = {}

        for folder in folders:
            if not folder.is_file():
                folder_name = folder.name
                folder_name_uppercase = folder_name.upper()

                if "DEV" in folder_name_uppercase:
                    continue

                elif "ORA" in folder_name_uppercase:
                    ora_version = int("".join(filter(str.isdigit, folder_name)))
                    found_ora[ora_version] = folder_name

                elif "KIA" in folder_name_uppercase:
                    kia_version = int("".join(filter(str.isdigit, folder_name)))
                    found_kia[kia_version] = folder_name

        move_to_archive(source_folder, archive_folder, found_ora)
        move_to_archive(source_folder, archive_folder, found_kia)


def move_to_archive(source_folder, archive_folder, versions_dict):
    if len(versions_dict) > 0:
        highest_version = max(versions_dict.keys())
        for folder in versions_dict.values():  # Iterate through the folder names
            version = int("".join(filter(str.isdigit, folder)))
            if version < highest_version:
                source_path = os.path.join(source_folder, folder)
                shutil.move(source_path, os.path.join(archive_folder, folder))
                print(f"Moved {folder} to {archive_folder}")


if __name__ == "__main__":
    # start = datetime.datetime.now()
    main()
    # finish = datetime.datetime.now()
    # print (finish-start)
    input("Press Enter to Exit...")
