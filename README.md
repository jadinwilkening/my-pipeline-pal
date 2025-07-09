# My Pipeline Pal

A Python script to help organize animation project files by type and generate a file log.

## What It Does
- Scans a folder of files (like a film or animation project)
- Sorts files into folders like `/audio`, `/scenes`, `/images`
- Logs each file’s name, type, size, and destination into a CSV

## How to Use
1. Put your messy files in a folder called `sample_project`
2. Run the script
3. Check `organized_project/` for sorted files
4. Check `log.csv` for your file report

## How to Run
1. Clone this repository to your computer
If you have Git installed, run this in your terminal: https://github.com/jadinwilkening/my-pipeline-pal.git
2. Navigate into the project folder
3. Run the Python script:
python organize.py

## Why I Built This
Animation studios use lots of digital files. “My Pipeline Pal” makes file management easier, faster, and more studio-ready.

## Technologies
- Python 3
- CSV file writing
- File organization with `os` and `shutil`

