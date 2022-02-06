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

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze data.
    #read the file object 
    file_reader= csv.reader(election_data)

    # Print Header row. 
    headers = next(file_reader)
    print(headers)