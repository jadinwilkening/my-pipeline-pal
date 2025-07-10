import os
import shutil
import csv
from datetime import datetime
from view_log import print_log_table #custom to display csv log as a table
import argparse

#-----------------
#CONSTANTS#
#-----------------
# Maps known file extension to destination folder
#Directs files to destinations
FOLDER_MAP = {
    '.blend': 'scenes',
    '.wav': 'audio',
    '.mp4': 'video',
    '.jpg': 'images',
    '.png': 'images'
}

#-----------------
#HELPER FUNCTIONS#
#-----------------

def create_folders(dest_dir, folder_map):
    """
    Ensures all destination folders are created prior to sorting.
    This includes a 'misc' folder for unrecognized file types
    """
    for folder in set(folder_map.values()):
        os.makedirs(os.path.join(dest_dir, folder), exist_ok=True)
    os.makedirs(os.path.join(dest_dir, 'misc'), exist_ok=True)

def handle_duplicate(dest_path):
    """
    Handles naming conflicts when a file with the same name already exists
    """
    base, extension = os.path.splitext(dest_path)
    counter = 1
    original_path = dest_path
    while os.path.exists(dest_path):
        dest_path = f"{base}_{counter}{extension}"
        counter += 1
    return dest_path, dest_path != original_path

def organize_file(file_path, dest_dir, folder_map):
    """
    Determines the file type, assigns destination folder, and moves files accordingly
    """
    try:
        ext = os.path.splitext(file_path)[1].lower()
        size_kb = round(os.path.getsize(file_path) / 1024, 2)
        file_name = os.path.basename(file_path)
    except OSError as e:
        print(f"Error reading file: {file_path} ({e})")
        return None, False
    
    #Determines destination folder
    new_folder = folder_map.get(ext, 'misc')

    #Log unknown file types
    if new_folder == 'misc':
        ext_display = ext if ext else '[no extension]'
        print(f" Unknown File Type Detected: '{file_name}' (extension: {ext_display}) → sorted into 'misc' folder.")

    target_dir = os.path.join(dest_dir, new_folder)
    os.makedirs(target_dir, exist_ok=True)

    dest_path = os.path.join(target_dir, file_name)
    dest_path, was_renamed = handle_duplicate(dest_path)

    try:
        shutil.copy2(file_path, dest_path)
    except Exception as e:
        print(f"Error copying file: {file_path} → {dest_path} ({e})")
        return None, False

    if was_renamed:
        print(f" Duplicate found! Renamed '{file_name}' to '{os.path.basename(dest_path)}'")

    file_info = {
        "file_name": os.path.basename(dest_path),
        "ext": ext if ext else 'unknown',
        "size_kb": size_kb,
        "new_location": new_folder
    }

    return file_info, was_renamed

def log_file(writer, file_info):
    "Adds rows"
    writer.writerow([
        file_info['file_name'],
        file_info['ext'],
        file_info['size_kb'],
        file_info['new_location']
    ])

def generate_summary_log(log_file, summary_data):
    "Adds a summary to begining of csv log file"
    "Gives quick stats"
    summary_lines = [
        f"My Pipeline Pal Log Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total files processed: {summary_data['total']}",
        f" - Known File Types: {summary_data['known']}",
        f" - Unknown File Types: {summary_data['unknown']}",
        f"Duplicate Files Renamed: {summary_data['duplicates']}",
        f"Total Size: {round(summary_data['size_kb'] / 1024, 2)} MB",
        "-" * 40,
        ""
    ]

    try:
        with open(log_file, 'r') as original:
            original_lines = original.readlines()

        with open(log_file, 'w') as modified:
            for line in summary_lines:
                modified.write(line + "\n")
            modified.writelines(original_lines)
    except Exception as e:
        print(f"Error generating summary log: {e}")


#--------------------------
#MAIN EXECUTION FUNCTION#
#--------------------------

def main():
    "Parses CLI arguments, creates folders, checks files in source directory,"
    "organizes the files, and logs the activity"
    parser = argparse.ArgumentParser(description="Organize files by type for animation pipeline.")
    parser.add_argument('--source', default='sample_project', help='Source directory to organize')
    parser.add_argument('--dest', default='organized_project', help='Destination directory for organized files')
    parser.add_argument('--log', default='log.csv', help='Path to log CSV file')
    args = parser.parse_args()

    source_dir = args.source
    dest_dir = args.dest
    log_path = args.log 

    #For data in Final Summary
    total_files = known_files = unknown_files = duplicates = total_size_kb = 0

    create_folders(dest_dir, FOLDER_MAP)

    #Write log file
    with open(log_path, 'w', newline='') as csvfile: 
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'File Extension', 'File Size (KB)', 'Sorted Into Folder'])

        #Go through all files in source directory 
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                info, was_renamed = organize_file(file_path, dest_dir, FOLDER_MAP)
                if info is None:
                    continue
                
                #Update metrics
                total_files += 1
                total_size_kb += info['size_kb']
                if info['new_location'] == 'misc':
                    unknown_files += 1
                else:
                    known_files += 1
                if was_renamed:
                    duplicates += 1

                log_file(writer, info) #log each file's data

    #Final summary and log print
    summary = {
        "total": total_files,
        "known": known_files,
        "unknown": unknown_files,
        "duplicates": duplicates,
        "size_kb": total_size_kb
    }

    generate_summary_log(log_path, summary)
    print_log_table(log_path) #Print table in terminal

#Run script only when told
if __name__ == "__main__":
    main()
