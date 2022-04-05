# Python-challenge
Repository to demonstrate Python exercises 

##Overview:
	Before developing a report, an essential starting point is understanding the needs and expectations of your customer. Your customer could be internal or external, significantly changing your approach. In this scenario, we assume that our customer is internal and therefore has a basic understanding of the data and will be able to understand the information presented in our report quickly. This assumption allows us to generate a direct report without many visualizations. We anticipate that the user will be comfortable moving around and manipulating the information. 

	In this example, we will be building two reports. The first report is based on the budget_data .csv file from the PyBank data. This report will develop a financial analysis based on the profits and losses from each month listed within the file. Take a moment to open the .csv file and familiarize yourself with the data structures and layout. 
	We begin our Python script by importing the necessary dependents that will enable us to perform the required functions within the script. This is an important step, as these additional modules will make processing the data more accessible. We then connect to the .csv file and read the data into our program. We will then use several 'for-loops' to review the data and develop our calculations for totals and the changes that occurred between the profit and loss for each month. Once these foundational calculations are complete, we can then build our secondary analyses used in our final report. 
	The final report is printed as output in the last portion of the script, and a copy of the report is exported to a .txt file. This fill will be added to the same folder as the script. 
	
	For the second portion report, we will construct a voting analysis based on the election_data file located in the Resources folder of the PyPoll folder. Similar to the financial analysis earlier, we begin our Python script by importing the necessary dependents that will enable us to perform the required functions within the script. We then connect to the .csv file and read the data into our program. We will then use several 'for-loops' to review the data, develop our calculations for totals for votes, and create a dictionary containing the candidates listed within the data and the number of votes they received. The candidates will be the keys to the dictionary, and the total number of votes for each candidate will be the value. Once the foundational analysis is done, we can use the variables that contain that information to create the summary report. One important note is that due to the layout required by the report, we need to use an additional loop and 'f-strings' to format the needed output properly. 
	As we did for the financial analysis, once the report is printed, a copy is also created in a .txt file and saved to the same folder as the python script. 
	
##Key Development Instructions:

#Financial Analysis Instructions
Create a Python script to analyze the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

Your analysis should look similar to the following:
```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Voter Polling Instructions

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

Your analysis should look similar to the following:

```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```
 
In addition, your final script should both print the analysis to the terminal and export a text file with the results.