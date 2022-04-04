# Import dependencies 
import os
import csv
import pandas as pd


# Create the connection to the csv file with source data

original_file = 'Resources/election_data.csv'

Candidates_df = pd.read_csv(original_file)

#Create variables that will be used to house the data needed for tracking totals within the loops
#Also create variables that will capture the values that need to be reported 

Total_votes = Candidates_df["Ballot ID"].count()



Candidates_df["Vote_Perc"] = ((1 / Total_votes)*100)

Candidate_Votes = Candidates_df["Candidate"].value_counts()
Candidate_Perc = (Candidate_Votes / Total_votes) * 100
#Winner = Candidates_df.loc[]
Summary_df = pd.DataFrame({"Perc ": Candidate_Perc,"Votes": Candidate_Votes})

print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_votes}")
print("-------------------------")
print(Summary_df)


Candidates_dict = {}


#Open the csv file to begin working on the data.
#Notice we also create a variable (input_file) for the opened file that will be used throughout the program
# input_file = open(original_file)
# input_file = csv.reader(input_file, delimiter=",")
# csv_header = next(input_file)

# for line in input_file:
#     Total_votes += 1
#     Candidates_dict[line[2]] = 0
   




