import csv

import os

 

source_file = "changename.csv"

destination_file = "changename.csv"

line_number = 807  # Change this to the line number you want to export

start_directory = "C:\\path\\to\\data\\here"

 

os.chdir(start_directory)

 

with open(source_file, "r") as source, open(destination_file, "w", newline="") as dest:

    reader = csv.reader(source)

    writer = csv.writer(dest)

   

    for index, row in enumerate(reader):

        if index == line_number - 1:

            writer.writerow(row)

            break
