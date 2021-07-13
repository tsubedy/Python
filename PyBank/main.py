# Budget Analysis

import os
import csv

# data files to read
data_file = os.path.join('.', 'Resources', 'budget_data.csv')

# Output file to store results 
output_file = os.path.join('.', 'Analysis', 'budget_data_analysis.txt')

# initialize variables

months_of_change = []
actual_change_list = []
max_increase = ["", 0]  # Compare with the lowest possible
max_decrease = ["", 99999999999999999999]  # Compare with the highest possible

total_change = 0

# Read budget_data.csv
with open(data_file) as budget_data:
    reader = csv.reader(budget_data)

    # read the header row
    header = next(reader)
    # print(f"Header: {header}")  # Reading the header of the data file

    # Extract the first row
    first_row = next(reader)
    # print(first_row)

    # for the first month (starts from month = 1)
    total_months = 1
    total_change = total_change + int(first_row[1])

    # assigning the value form first row as a previous net change
    prev_net = int(first_row[1])

    # loop through the data from the 2nd row

    for row in reader:
        # tracking the total months
        total_months = total_months + 1

        # tracking the total change
        total_change = total_change + int(row[1])

        # tracking the net change
        actual_change = int(row[1]) - prev_net
        prev_net = int(row[1])

        # putting actual change in the list
        actual_change_list = actual_change_list + [actual_change]

        # putting actual months of change in the list
        months_of_change = months_of_change + [row[0]]

        if actual_change > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[1] = actual_change

        if actual_change < max_decrease[1]:
            max_decrease[0] = row[0]
            max_decrease[1] = actual_change

    # Calculate the average net changes
    net_monthly_average = sum(actual_change_list) / len(actual_change_list)

    output = (
        f"\nBudget Analysis\n"
        f"======================================================\n"
        f"Total number of months: {total_months}\n"
        f"Total amount:     ${total_change}\n"
        f"Average change:   ${net_monthly_average:.2f}\n"
        f"Greatest increase in profits of ${max_increase[1]}, in {max_increase[0]}\n"
        f"Greatest decrease in profits of ${max_decrease[1]}, in {max_decrease[0]}\n"
        f"======================================================\n"
    )
    print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)
