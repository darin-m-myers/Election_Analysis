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
- There were __369,711__ votes cast in the election
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham recieved __23.0%__ of the vote with __85,213__ votes.
    - Diana DeGette recieved __73.8%__ of the vote with __272,892__ votes.
    - Raymon Anthony Doane recieved __3.1%__ of the vote with __11,606__ votes.
- The winner of the election was:
    - __Diana DeGette__, who recvieved __73.8%__ of the vote with __272,892__ votes.
    
- The voter turnout for each county was:
    - Jefferson had __10.5%__ of the total with __38,855__ voters.
    - Denver had __82.8%__ of the total with __306,055__ voters.
    - Arapahoe had __6.7%__ of the total with __24,801__ voters.

- __Denver__ had the highest turnout with __82.8%__ of the total with __306,055__ voters.

## Election - Audit Summary
The script was created to analyze the election results and is fairly robust. If the raw data is in a similar setup it could be applied to any election made up of counties. There are two additonal opportunities that I see for using this script in other types of elections:
 1. This could be adjusted to be used in a School Board Elections and the summary could be adjusted to provide a breakout by candidate and school zone
 2. This could be adjusted to be used in County Sherrif Elections and the summary could be adjusted to provide a breakout by candidate and precinct
 
Depending on the adjustments, there are likely additional opportunites available.
