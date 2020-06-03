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
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)

    #num_votes = 0
    potential_candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0


    for i in open(csvpath):
        #the_candidate = row[2]
        if i == "Khan":
            Khan_votes = Khan_votes + 1
        elif i == "Correy":
            Correy_votes = Correy_votes + 1
        elif i == "Li":
            Li_votes = Li_votes + 1
        elif i == "O'Tooley":
            OTooley_votes = OTooley_votes + 1

percent_Khan = Khan_votes / num_votes * 100
percent_Correy = Correy_votes / num_votes * 100
percent_Li = Li_votes / num_votes * 100
percent_OTooley = OTooley_votes / num_votes * 100


# The winner of the election based on popular vote.
percentage_list = [percent_Khan, percent_Correy, percent_Li, percent_OTooley]
winner = max(percentage_list)


# Export the outputs; the txt file is in the "analysis" folder
export_output = (
    f"\nElection Results\n" 
    f"-------------------------\n" 
    f"Total Votes: {num_votes}\n" 
    f"-------------------------\n"
    f"Khan: {percent_Khan}% ({Khan_votes})\n"
    f"Correy: {percent_Correy}% ({Correy_votes})\n"
    f"Li: {percent_Li}% ({Li_votes})\n"
    f"O'Tooley: {percent_OTooley}% ({OTooley_votes})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
    )

print (export_output)

with open(outputpath, "w") as txt_file:
    txt_file.write(export_output)
