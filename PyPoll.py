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

# Candidate options and candidate votes
candidate_options=[]
#Declare the empty dictionary.
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
        # Print the candidate name from each row.
        candidate_name = row[2]

        #Check if candidate name is in the array 
        if candidate_name not in candidate_options:
            # Add the candidates name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate's vote count.
        candidate_votes[candidate_name] += 1
#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the dandiate list.
for candidate_name in candidate_votes:
    # Retrieve vote4 count of a candidate 
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes)*100
    #Print the candidates name and percentage of votes.
    print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")
    
    #Determine winning vote count and candidate
    #Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true than set winning_count = votes and winning percentage=vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #Set winning candidate equal to the candidates name
        winning_candidate = candidate_name

winning_candidate_summary=(
    f"-------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------\n")
print(winning_candidate_summary)