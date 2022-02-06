#Data we need to retrieve.
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote
#Resources/election_results.csv

# Add dependencies.
import csv
import os

# Assign a variable for the file to load.
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable for the file to save.
file_to_save = os.path.join("analysis", "elections_analysis.txt")

# Inititize a total vote counter.
total_votes = 0


candidates_options=[]

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object 
    file_reader= csv.reader(election_data)

# To do: read and analyze data.
    # Read the header row.
    headers = next(file_reader)

    # Print Header row. 
    for row in file_reader:
        # Add to the total vote count.
        total_votes+=1
        #Print the candidate name from each row.
        candidate_name = row[2]

        # Add the dandidates name to the dandidate list
        candidates_options.append(candidate_name)

print(candidates_options)