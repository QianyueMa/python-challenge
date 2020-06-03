# Dependencies
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')
outputpath = os.path.join('..', 'PyPoll', 'analysis', 'election_analysis.txt')


# The total number of votes cast
with open(csvpath) as csvfile:
    num_rows = 0
    for row in open(csvpath):
        num_rows += 1

num_votes = num_rows - 1 # Not counting the header row of the sheet
print(f"Total Votes: {num_votes}") 


# A complete list of candidates who received votes as well as their winning percentage and the total number of votes each candidate won
#   use list.append() to track the list
with open(csvpath) as csvfile:
    revenue = csv.reader(csvfile)
    csv_header = next(revenue)

    num_votes = 0
    potential_candidates = []
    gained_votes = {}


    for row in open(csvpath):
        num_votes = num_votes + 1
        candidate = row[2]
        if candidate not in potential_candidates:
            potential_candidates.append(candidate)

            gained_votes[candidate] = 0

        gained_votes[candidate] = gained_votes[candidate] + 1

print (gained_votes)






# The winner of the election based on popular vote.

