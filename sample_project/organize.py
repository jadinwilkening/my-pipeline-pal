import os
import shutil
import csv


SOURCE_DIR = "sample_project"
DEST_DIR = "organized_project"
LOG_FILE = "log.csv"

# Map of file extensions to folders
FOLDER_MAP = {
    '.blend': 'scenes',
    '.wav': 'audio',
    '.mp4': 'video',
    '.jpg': 'images',
    '.png': 'images'
}

# Create folders
for folder in set(FOLDER_MAP.values()):
    os.makedirs(os.path.join(DEST_DIR, folder), exist_ok=True)

# Create CSV log file
with open(LOG_FILE, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Name', 'Type', 'Size (KB)', 'New Location'])

    # Go through files in source folder
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            file_path = os.path.join(root, file)
            size_kb = round(os.path.getsize(file_path) / 1024, 2)

            # Move known types
            if ext in FOLDER_MAP:
                new_folder = FOLDER_MAP[ext]
                dest_path = os.path.join(DEST_DIR, new_folder, file)

                shutil.copy2(file_path, dest_path)

                # Write log row
                writer.writerow([file, ext, size_kb, new_folder])
