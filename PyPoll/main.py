# PyPoll code



#* The total number of votes cast

#* A complete list of candidates who received votes

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

##* The winner of the election based on popular vote.

#Your analysis should look similar to the following:


 # ```text
  #Election Results
 # -------------------------
 #Total Votes: 369711
  #-------------------------
  #Charles Casper Stockham: 23.049% (85213)
  #Diana DeGette: 73.812% (272892)
  #Raymon Anthony Doane: 3.139% (11606)
  #-------------------------
  #Winner: Diana DeGette
  #-------------------------
  #```



#dependencies

import os
import csv


# Path for resource file

Poll_csv = os.path.join( "Resources", "election_data.csv")

#create lists to store data

candidate = []

#open csv and populate the lists with data
with open(Poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)

    for row in csvreader:

        # add candidate data
        candidate.append(row[2])

#define variables and count votes
diana_votes = 0 
charles_votes = 0
anthony_votes = 0
for i in candidate:
    if i == 'Diana DeGette':
        diana_votes = diana_votes + 1
    if i == 'Charles Casper Stockham':
        charles_votes = charles_votes + 1
    if i == 'Raymon Anthony Doane':
        anthony_votes = anthony_votes + 1

# calculate total an %s
per_diana = 0
per_charles = 0
per_anthony = 0

total = len(candidate)
per_diana = round(100 * diana_votes / total ,2)
per_charles = round(100 * charles_votes / total ,2)
per_anthony = round(100 * anthony_votes / total ,2)

candidate_votes = [diana_votes,charles_votes,anthony_votes]
candidate_names = ['Diana DeGette', 'Charles Casper Stockham', 'Anthony Doane']

winner_index = candidate_votes.index(max(candidate_votes))
winner_name = candidate_names[winner_index]

#print results

analysis_out =("Election results\n"
"____________________________\n"
f"Total votes: {total}\n"
"____________________________\n"
f"Charles Casper Stockham: {per_charles}% ({charles_votes})\n"
f"Diana DeGette: {per_diana}% ({diana_votes})\n"
f"Raymon Anthony Doane: {per_anthony}% ({anthony_votes})\n"
"____________________________\n"
f"Winner: {winner_name}\n"
"____________________________\n"
)


print(analysis_out)


# create txt file

results = os.path.join("Analysis","PyPoll_Analysis.txt")

with open(results, "w") as textfile:
    textfile.write(analysis_out)


