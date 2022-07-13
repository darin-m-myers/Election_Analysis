# Import the Data
import csv

import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_load, 'r') as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        # Print the header row.
        headers = next(file_reader)
        print(headers)

    # Count the total number of votes cast

    # Record the names for all the candidates

    # Record the total votes for each candidate

    # Record the percentage of votes each candidate won

    # Provide a results of the election

