# Import dependencies 
import os
import csv
import sys


# Create the connection to the csv file path with source data

csvpath = os.path.join("Resources","election_data.csv")

# Create variables that will track/hold the calculated values from the loops
Candidates = {}
Total_Votes = 0

# Open the csv file 
csvfile = open(csvpath)

# 'Read-in' the source data from the csv file
csvreader =csv.reader(csvfile, delimiter=",")

# Skip the first row of the data since this row contains headers
csv_header = next(csvreader)

# Begin look to calculate the total number of votes, by counting the number of rows/records in the data
# Loop through the data in the third column to determine the names of the candidates that need to be 
# added to the Candidates dictionary. We also capture the number of votes for each candidate and add that value as the values for the keys/candidates 
for line in csvreader:
    Total_Votes += 1
    if line[2] not in Candidates:
        Candidates[line[2]] = 1
    else:
        Candidates[line[2]] += 1

# Print the summary report
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------")

# Loop that will properly display the candidates, the percentage of votes won, and the total votes won per candidate
for key,value in Candidates.items():
    print(f"{key}:",f"{round((value/Total_Votes)*100,3)}%",f"({value})")
print("-------------------------")
print(f"Winner: {max(Candidates,key=Candidates.get)}")
print("-------------------------")

# Save a reference point for the original Financial Analysis
original_stdout = sys.stdout # Save a reference point for the original Financial Analysis

# Create a txt file for a copy of the output. This will be placed in the same 
#folder as the .py file
with open('main_output.txt', 'w') as f:
    sys.stdout = f 
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {Total_Votes}")
    print("-------------------------")
    for key,value in Candidates.items():
        print(f"{key}:",f"{round((value/Total_Votes)*100,3)}%",f"({value})")
    print("-------------------------")
    print(f"Winner: {max(Candidates,key=Candidates.get)}")
    print("-------------------------")
    # Reset to the origial output
    sys.stdout = original_stdout 