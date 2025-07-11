# My Pipeline Pal

**My Pipeline Pal** is a Python tool designed to help artists, animators, and creatives quickly organize their project files by type, automatically sorting and logging files into appropriate folders. It’s especially useful in animation pipelines to keep large directories clean, organized, and easy to navigate.

---

## Features

- Automatically sorts files by extension into folders like `scenes`, `audio`, `video`, `images`, or `misc` for unknown types  
- Handles duplicate file names gracefully by renaming copies with numbered suffixes  
- Generates a detailed CSV log with file names, types, sizes, and their new locations  
- Displays a formatted summary table of all organized files in the terminal using `tabulate`  
- Configurable source directory, destination directory, and log file via command-line arguments  
- Easy-to-understand components (`organize.py` and `view_log.py`)

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/jadinwilkening/my-pipeline-pal
    cd my-pipeline-pal
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Run the organizer script with optional arguments:

```bash
python organize.py --source <source_folder> --dest <destination_folder> --log <log_file.csv>
```

---

## Example
An example organizer script:

```bash
python organize.py --source sample_project --dest organized_project --log log.csv
```

If no arguments are provided, defaults are used:

    source: sample_project

    dest: organized_project

    log: log.csv

---

## Sample Output

Here’s a screenshot of the log summary displayed in the terminal:

![Terminal Display][images/TerminalDisplay.png]

Here’s how the CSV log file looks when opened:

![CSV Table Display][images/CSVTableDisplay.png]


## Project Structure
my-pipeline-pal/
│
├── organize.py       # Main script to organize files
├── view_log.py       # Display CSV log as table
├── README.md         # This file
└── sample_project/   # Example folder with files to organize

## Dependencies

Install these:
    Python 3.6+
    tabulate

Install dependencies using in terminal:
```bash
        pip install -r requirements.txt
```

[images/TerminalDisplay.png]: images/TerminalDisplay.png
[images/CSVTableDisplay.png]: images/CSVTableDisplay.png