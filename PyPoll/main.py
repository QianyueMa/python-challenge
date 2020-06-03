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
    reader = csv.reader(csvfile)
    csv_header = next(reader)

    #num_votes = 0
    potential_candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    Khan_votes = 0
    Correy_votes = 0
    gained_votes = {}
'''
    winning_candidate = ""
    winning_count = 0
'''

    for i in potential_candidates:
        if i == "Khan":
            Khan_votes = Khan_votes + 1
        elif i == "Correy":
            Correy_votes = Correy_votes + 1
        elif i == "Li":
            Li_votes = Li_votes + 1
        elif i == "O'Tooley":
            OTooley_votes = OTooley_votes + 1



    for row in open(csvpath):
        num_votes = num_votes + 1
        the_candidate = row[2]
        if the_candidate not in potential_candidates:
            potential_candidates.append(the_candidate)

            gained_votes[the_candidate] = 0

        gained_votes[the_candidate] = gained_votes[the_candidate] + 1

    for i in gained_votes:
        votes = gained_votes.get(i)
        vote_percentage = float(votes) / float(num_votes) * 100
        if (votes > winning_count):
            winning_count = votes 
            winning_candidate = i
print(winning_candidate)
    

    







# The winner of the election based on popular vote.


'''
# Export the outputs; the txt file is in the "analysis" folder
output = (
    f"\n\nElection Results\n" 
    f"-------------------------\n" 
    f"Total Votes: {total_votes}\n" 
    f"-------------------------\n")
print(output, end="")
'''