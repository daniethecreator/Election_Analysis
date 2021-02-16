# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the elections audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Stuio Code, 1.38.1

## Summary
The analysis of the elections show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 - The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
 - The winner of the elections was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes
  
 ## Challenge Overview
The Colorado Board of Elections employee has asked for a few additional data in order to complete the audit in the local election. They requested the following:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Challenge Results
The following election outcomes were asked to be addressed. 

* How many votes were cast in this congressional election?
   - The total number of votes in the congressional election was 369,711. This was discovered after initializing a vote counter "total_votes = 0". Then I created a variable and a path to the csv file using "file_to_load = os.path.join("Resources", "election_results.csv"). After the file_to_load had the path to the election_results.csv file, I opened the csv file using a with statement, "with open(file_to_load) as election_data" and then iterated over each row of the file adding 1 to the total vote count "for row in reader: total_votes = total_votes + 1". The election_results variable was then printed in the terminal and in the txt_file "election_results = (f"Total Votes: [total_votes:,}\n)"
   
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.


* Which county had the largest number of votes?
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  -Winner: Diana DeGette
  -Winning Vote Count: 272,892
  -Winning Percentage: 73.8%


## Challenge Summary
* The script can be used with some modications for any election as long as the path to the file is updated and if the columns are the same. All that would be needed is to update the text inside the " " in the file_to_load = os.path.join("Resources", "election_results.csv") and file_to_save = os.path.join("analysis", "election_analysis.txt") with the new file location that would be used to pull the data from and a new file created to not override the existing data. Also, depending on what column contains the name or county would need to be updated when the code calls out the "row" for example, candidate_name = row[2], but if it was in the first column, then it could be updated with row[0]. 
