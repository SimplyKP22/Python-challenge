# Import the dependencies
import os
import csv
import sys

# Create the connection to the csv file with source data
original_file = 'Resources/budget_data.csv'

#Create variables that will be used to house the data needed for tracking totals within the loops
#Also create variables that will capture the values that need to be reported  
 
Dates = []
Total_Months = 0
Profit_Losses = []
Total_Profit_Loss = 0
Change_list = []
TotalOfChanges = 0
Greatest_Increase_Date = ""
Greatest_Decrease_Date = "" 

#Open the csv file to begin working on the data.
#Notice we also create a variable (input_file) for the opened file that will be used throughout the program
with open(original_file) as input_file:
    input_file = csv.reader(input_file, delimiter=",")
    csv_header = next(input_file)
    #Loop through the lines of the data and count the rows. This will give you the total number of rows which is also the
    #total number of months listed in the dataset. 

    for line in input_file:
        #For each line that is encountered, add 1 to the Month_Count tracker that we created
        #Record the date in the Dates list, and record the Profit/Loss in the Profit_Losses list 
        Total_Months += 1
        Dates.append(line[0])
        Profit_Losses.append(int(line[1]))

    #Calculate the total of the values in the Profit/Losses column(list).
    #Here we use the Total_Profit_Loss tracker to keep a track of the total as the loop iterates through the rows
    for record in Profit_Losses:
        Total_Profit_Loss += record

    for i in range(len(Profit_Losses)-1):
        Change_list.append(Profit_Losses[i+1]-Profit_Losses[i])

    for change in Change_list:
        TotalOfChanges += change

    Average_Change = round(TotalOfChanges/(Total_Months-1),2)
    Change_list.sort()
    Change_list_Length = len(Change_list)
    Greatest_Increase = Change_list[Change_list_Length-1]
    Greatest_Decrease = Change_list[0]
    
    for line in input_file:
        if line[1] == Greatest_Increase:
            Greatest_Increase_Date = line[0]
    
    for line in input_file:
        if line[1] == Greatest_Decrease:
            Greatest_Decrease_Date = line[0]
    


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: {Total_Profit_Loss}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})")


original_stdout = sys.stdout # Save a reference point for the original Financial Analysis

with open('main_output.txt', 'w') as f:
    sys.stdout = f # Create a txt file for a copy of the output. This will be placed in the same 
                    #folder as the .py file
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: {Total_Profit_Loss}")
    print(f"Average Change: ${Average_Change}")
    print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})")
    print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})")
    sys.stdout = original_stdout # Reset to the origial output