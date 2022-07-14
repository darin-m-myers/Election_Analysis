# Add our dependencies.
import csv

import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#### Begin Gathering Candiate Summary

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and Votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Initialize a county total vote counter.
total_county_votes = 0

# County Options and Votes
county_list = []
county_votes = {}

# Winning County and Winning Count Tracker
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        ### CANDIDATE DATA
        # Count the total number of votes cast
        total_votes += 1

        # Record the names for all the candidates
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Record the total votes for each candidate
        candidate_votes[candidate_name] += 1
        
        ### COUNTY DATA
        # Record the names for all the counties
        county_name = row[1]

        if county_name not in county_list:

            # Add it to the list of county.
            county_list.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Record the total votes for each county
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Set consisitent dashed line breaks
    horizontal_line = "-" * 25 + "\n"

    ### Election Summary Data
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"{horizontal_line}"
        f"Total Votes: {total_votes:,}\n"
        f"{horizontal_line}"
        f"\nCountyVotes:\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Record the percentage of votes each county
    for county_name in county_votes:

        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Provide a results of the election
        county_election_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county, their voter count, and percentage to the terminal.
        print(county_election_results)

        #  Save the county results to our text file.
        txt_file.write(county_election_results)

        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_county_count = votes
            winning_county_percentage = vote_percentage
            # And, set the winning_county equal to the county's name.
            winning_county = county_name   

    winning_county_summary = (
        f"\n{horizontal_line}"  
        f"Largest County Turnout: {winning_county}\n"
        f"{horizontal_line}")
    print(winning_county_summary)

    txt_file.write(winning_county_summary)
    

    ### CANDIDATE DATA
    # Initialize variables
    votes = 0
    vote_percentage = 0.0
    
    # Record the percentage of votes each candidate won
    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Provide a results of the election
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name   

    winning_candidate_summary = (
        f"{horizontal_line}"  
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{horizontal_line}")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)