# Budget Analysis

import os
import csv

# files to load and output

data_file = os.path.join('.', 'Resources', 'election_data.csv')
output_file = os.path.join('.', 'Analysis', 'election_data_analysis.txt')

# total votes casted
total_votes = 0

# List of Candidates to be elected (options)
candidates = []

# Candidate that was voted by each voters
candidates_voted = {}

# Name of the winning candidate and the number of votes received
winning_candidate = ""
winning_count = 0

# Read election_data.csv
with open(data_file) as election_data:
    reader = csv.reader(election_data)

# read the header row
    header = next(reader)
    print(f"Header: {header}")

    for row in reader:
        # counting total votes (each row is counted as a vote)
        total_votes = total_votes + 1

        # getting candidate's name from each row (index 2)
        candidate_name = row[2]
        candidates.append(candidate_name)

    # def unique(list1):
    #     # insert the list to the set
    #     list_set = set(list1)
    #     # convert the set to the list
    #     unique_list = (list(list_set))
    #     for x in unique_list:
    #         print(x)
    #
    # unique(candidates)
    #
    # from collections import Counter
    # z = Counter(candidates)
    # print(z)

    # if the name of the candidate is not already in the list, then keep adding to the list
    if candidate_name not in candidates:
        candidates.append(candidate_name)

        # track the vote counter for each candidates
        candidates_voted[candidate_name] = 0
        candidates_voted[candidate_name] = candidates_voted[candidate_name] + 1

with open(output_file, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"=======================\n"
        f"Total Votes: {total_votes}\n"
    )

print(election_results)

for winner in candidates_voted:
    votes = candidates_voted.get(winner)
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"percentage {vote_percentage}")
    print(f"Votes {votes}")

    # finding the winning candidate and their votes
    if votes > winning_count:
        winning_count = votes
        winning_candidate = winner

    voter_output = f"{winner}: {vote_percentage: .3f}% ({votes})\n"
    print(voter_output, end="")
