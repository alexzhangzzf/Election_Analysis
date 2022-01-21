# Election Analysis
## Overview of Election Audit
Colorado Board of Elections assign the task to complete an election audit of a recent local congressional election. They want a module to analyze election results using Python and need the information on total number of votes, list of candidates, total votes of each candidate, percentage of votes each candidate won, winner of the election based on votes, voter turnout of each county, percentage of votes from each county and county of highest turnout. We wrote a python programming script for the election audit which can also be applied for future election analysis. 
## Election-Audit Results
The analysis of the election shows as figure below:

![Election_results]( /Resources/Election_results.png)
- There were 369,711 total votes cast in the election.
- Votes and percentage of votes for each county in the precinct are:
   - Jefferson county received 38,855 votes which is 10.5% of the total vote.
   - Denver county received 306,055 votes which is 82.8% of the total vote.
   - Arapahoe county received 24,801 votes which is 6.7% of the total vote.
- County had the largest number of votes was:
   -Denver has the largest number of votes (306,055), which is 82.8% of total votes.
- Votes and percentage of votes for each candidate are:
   - Charles Casper Stockham received  85,213 votes which is 23.0% of the total votes.
   - Diana DeGette received 272,892 votes which is 73.8% of the total votes.
   - Raymon Anthony Doane received 11,606 votes which is 3.1% of the total votes.
- Winner of the election was:
   - Candidate Diana DeGette won the election with 272,892 votes which is 73.8% of the total votes.
## Election-Audit Summary
We proposed that this python script can be utilized for any future election analysis with modifications. It can be used to analyze election results for local election or national election, depending on the format and name of the data source. 
- For different file location or file name, we can modify the code `file_to_load = os.path.join("Resources", "election_results.csv")`, change the folder name and file name, from resources to folder name and election_results to the any source data name. `file_to_load = os.path.join("Resources folder", "election source data.csv")`.
- Depending on the kind of election, we can also modify the output for county to any region, for example, states for national election.
`county_results = (f"{state_name}: {state_percentage:.1f}% ({state_vote_count:,})\n")`
- Another possible modification for this code is to read data from each row. Depending on the data source layout, if the cell format is different, we can modify the row cell location for candidate name and county name from figure below to `row[candidate_column]`, `row[region_column]`.
![modification_row]( /Resources/modification_row.png)
With minor modifications we can use the same script to analyze any election results for audit.

   
   




