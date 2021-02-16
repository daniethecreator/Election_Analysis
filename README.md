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
The Colorado Board of Elections employee has asked for a few additional data requests in order to complete the audit in the local election. They requested the following:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Challenge Results
The following election outcomes were asked to be addressed. 

* How many votes were cast in this congressional election?
   * The total number of votes in the congressional election was 369,711. This was discovered after initializing a vote counter `total_votes = 0`. Then I created a variable and a path to the csv file using `file_to_load = os.path.join("Resources", "election_results.csv")`. After the `file_to_load` variable had the path to the `election_results.csv` file, I opened the csv file using a with statement, `with open(file_to_load) as election_data:` and then iterated over each row of the file adding 1 to the total vote count for each row `for row in reader: total_votes = total_votes + 1`. The `election_results` variable was then used to store the formated string containing the `total_votes` variable and was printed to the terminal and written to the `analysis/election_analysis.txt` file
```python
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    txt_file.write(election_results)
```
   
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  * After counting the votes for each county, I created a variable `county_vote_percentage` to calculate the percentage of votes by dividing the number of votes for each county by the total number of votes. This was thend multiplied by 100 and then formatted to show as a percentage next to each county and to have the corresponding total votes after the percentage. 

```python 
for county_name in county_dict:
        county_vote_count = county_dict[county_name]
        county_vote_percentage = float(county_vote_count)/float(total_votes) *100
        county_vote_results = county_vote_results + (f"{county_name}: {county_vote_percentage:.1f}% 
        print(county_vote_results, end="")
    txt_file.write(county_vote_results)
```

Below were the results of the votes by county

- County Votes:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)

* Which county had the largest number of votes?
 * Since I already had the total number of votes of each county, calculating which county had the largest of votes required comparing a county to the next county to see which one had the most votes and after comparing all the counties, printing the county as the same format as the votes by county. 

```python
        if county_vote_count > largest_county_vote:
             largest_county = county_name
             largest_county_vote = county_vote_count
        print(largest_county_results)
        txt_file.write(largest_county_results
 ```
 
 Denver was the largest county and was printed as follows: 
 Largest County Turnout: Denver
  
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
 * In order to get the votes each candidate received I iterated over the `candidate_votes` dictionary then I created a variable `vote_percentage` to calculate the percentage of votes by dividing the number of votes for each candidate by the total number of votes. This was then multiplied by 100 and then formatted to show as a percentage next to each candidate name and to have the corresponding total votes after the percentage.

```python
for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
 ```
 
 Below were the results of the votes by candidate
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
 * To find the candidate that won the election, I used the `winning_count` and `winning_percentage` variables I created earlier in the code to determine if a candidate had more votes and a higher voter percentage than another candidate as I went through the dictionary `candidate_votes` containing the candidate name and their vote counts. I then formatted it to print the winner and a summary of their vote count and percentage to the terminal and the text file. 

```python
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
```
 Below is how the winner summary looked in the terminal and text file: 
 
   Winner: Diana DeGette
   Winning Vote Count: 272,892
   Winning Percentage: 73.8%


## Challenge Summary
* The script can be used with some modications for any election as long as the columns are consistent. All that would be needed is to update the script to accept user input for the csv file to be read and, optional, the location of the election results output file while defaulting to `./output/election_results.csv` if not provided by the user. This script could also be refactored to remove redundant code by leveraging methods/functions thereby simplifying the code. 
