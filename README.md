# Election_Analysis

## Project Overview
The Colorado Board of Elections has requested the following detail to complete the election audit of a recent local congressional election:

1. The total number of votes cast
2. The complete list of candidates who recieved votes
3. The total number of votes each candidate won
4. The percentage of votes each candidate won
5. The winner of the election based on popular vote
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.9, Visual Studio Code 1.69.0

## Election - Audit Results
The analysis of the election show that:
- There were "369,711" votes cast in the election
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham recieved "23.0%" of the vote and "85,213" number of votes.
    - Diana DeGette recieved "73.8%" of the vote and "272,892" number of votes.
    - Raymon Anthony Doane recieved "3.1%" of the vote and "11,606" number of votes.
- The winner of the election was:
    - Diana DeGette, who recvieved "73.8%" of the vote and "272,892" number of votes.
    
- The voter turnout for each county was:
    - Jefferson had "10.5%" of the total count and "38,855" number of voters.
    - Denver had "82.8%" of the total count and "306,055" number of voters.
    - Arapahoe had "6.7%" of the total count and "24,801" number of voters.
- Denver had the highest turnout with "x%" of the total count and "y" number of voters.

## Election - Audit Summary
The script was created to analyze the election results and is fairly robust. If the raw data is in a similar setup it could be applied to any election made up of counties. There are two additonal opportunities that I see for using this script in other types of elections:
 1. This could be adjusted to be used in a School Board Elections and the summary could be adjusted to provide a breakout by candidate and school zone
 2. This could be adjusted to be used in County Sherrif Elections and the summary could be adjusted to provide a breakout by candidate and precinct
 
Depending on the adjustments, there are likely additional opportunites available.
