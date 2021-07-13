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

# Name of the winning candidate and the number of votes received
candidate_voted = ""


# Read election_data.csv
with open(data_file) as election_data:
    reader = csv.reader(election_data)

    # read the header row
    header = next(reader)
    print(f"Header: {header}")

    for row in reader:
        # counting total votes (each row is counted as a vote)

        # getting candidate's name from each row (index 2)
        candidate_voted = row[2]
        candidates.append(candidate_voted)
    # print(candidates)
    def counting(items):
        d = {}
        for i in items:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        return d

    # Counting votes for each candidates
    z = counting(candidates)
    # print(f"Vote counts for each candidates:  {z} ")  # name of the candidates with number of votes received

    # List of Name of the candidates
    for i in z:
        l = (i, z[i])
        print("The number of votes:", l)
    a1 = list(z.keys())
    # print(f"Candidates {a1} ")


    a = list(z.values())
    # print(f"Count of Votes:  {a} ")  # List of number of votes received by each candidate

    # Total votes counted
    t = sum(a)




    print(f"=======================")
    print(f"Total votes casted {t}")

    # Calculating percentages
    percentage = []
    for candidate, vote in z.items():
        z[candidate] = (vote / t) * 100
        percentage = z[candidate]

        # print(percentage)

        # print(f"votes received by {a[1]}:  {a[0]},  {percentage: .2f} ")
        # print("Percentages of votes", percentage)

    maximum = max(z, key=z.get)
    winner = (maximum, z[maximum])

with open(output_file, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"=======================\n"
        f"Total Votes: {t}\n"
        # f"votes by candidates {z}\n"
        f"Votes received by \n"
        
        f" {a1[0]}:  {a[0]}, {winner[1]:.2f}\n"
        
        f"The winner is : {winner[0]} who got {winner[1]:.2f}"

    )
# print(election_results)
