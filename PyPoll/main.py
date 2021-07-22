# Budget Analysis
import os
import csv

# files to load and output
data_file = os.path.join('.', 'Resources', 'election_data.csv')
output_file = os.path.join('.', 'Analysis', 'election_data_analysis.txt')

# total votes casted
total_votes = 0
candidates = {}
candidate_percentage = {}

# Read election_data.csv
with open(data_file) as election_data:
    reader = csv.reader(election_data)

    # read the header row
    header = next(reader)
    print(f"Header: {header}")

    for row in reader:
    # getting candidate's name from each row (index 2)
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] = candidates[candidate_name] + 1

    # print(candidates)
    total_votes = sum(candidates.values())
    # print(total_votes)

    for key, value in candidates.items():
        candidate_percentage[key] = (value /total_votes) * 100

    # print(candidate_percentage)

with open(output_file, "w") as txt_file:

    output = ""
    for key, value in candidate_percentage.items():
        output += key + ": " + "{:.3f}".format(value) + "% (" + str(candidates[key]) + ")\n"

    maximum = max(candidate_percentage, key=candidate_percentage.get)
    winner = (maximum)

    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"{output}"
        f"-------------------------\n"
        f"Winner: {winner} \n"
        f"-------------------------\n"
    )
    txt_file.write(election_results)

print(election_results)
