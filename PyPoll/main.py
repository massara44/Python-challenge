# Importing modules    
import os
import csv


#loading file
pypoll_path = os.path.join("Resources", "election_data.csv" )

#variable for candidates
candidates = []
#variable for number of votes for each candidate
candidate_votes = {}
#variable for the percentage of total votes each candidate
percent_votes = {} 
#variable for total number of votes 
total_votes = 0
#variable for winner's votes
winner_votes = 0
#variable for winner
winner = []


with open(pypoll_path, newline="") as file:
    csv_reader = csv.reader(file, delimiter=",")
    header = next(csv_reader)

    # tally votes
    for row in csv_reader:
        total_votes += 1
        candidates = row[2]
        if candidates in candidate_votes:
            candidate_votes[candidates] += 1
        else:
            candidate_votes[candidates] = 1

# calculate vote percentage and identify winner
for person, vote_count in candidate_votes.items():
    percent_votes[person] = (vote_count/total_votes) * 100
    percent_votes[person] = round(percent_votes[person])
    percent_votes[person] = "%.3f%%" % percent_votes[person]

    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person
        


# print out results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for person, vote_count in candidate_votes.items():
    print(f"{person}: {percent_votes[person]} ({vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")







