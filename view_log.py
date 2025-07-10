import csv
from tabulate import tabulate #Prints table in Terminal
import argparse #Command line argument parsing

def print_log_table(log_file):
    "Reads the csv file log and displays contents in a table"
    "Locates the header row named File Name to begin data"
    try:
        with open(log_file, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader) #Converts csv file to list or rows
    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading log file: {e}")
        return

    # Finds the header row index by searching for row that contains File Name
    header_index = next((i for i, row in enumerate(rows) if "File Name" in row), None)

    if header_index is not None:
        header = rows[header_index] #Grabs header row
        data = rows[header_index + 1:] #grabs data rows below header
        print("\nFile Organization Log:\n")
        print(tabulate(data, headers=header, tablefmt="fancy_grid")) #Display with borders
    else:
        print("No file log data found to display.")

#-------------------------
#MAIN EXECUTION FUNCTION#
#--------------------------

if __name__ == "__main__":
    #Adds CLI support to allow user to pass in a --log argument
    parser = argparse.ArgumentParser(description="Display file organization log.")
    parser.add_argument('--log', default="log.csv", help="Path to log CSV file")
    args = parser.parse_args()
    print_log_table(args.log)

