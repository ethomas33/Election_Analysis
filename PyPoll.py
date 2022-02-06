#Data we need to retrieve.
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote
#Resources/election_results.csv

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)

#Creat a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "elections_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save,"w")

#write some data to the file
outfile.write("Hello World")

#close the file
outfile.close()