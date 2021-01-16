#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:58:54 2021

@author: ron manipol
"""
import os
import csv

# Path to collect data from the Resources folder

poll_csv = os.path.join(os.getcwd(),"Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

#variables
total_votes = 0
list_of_candidates = []
total_candidates_votes = {}


# Read in the CSV file
csvfile = open(poll_csv, 'r')
csv_reader = csv.reader(csvfile, delimiter=',')

header = next(csv_reader)
for row in csv_reader:
    #The total number of votes cast
    total_votes = total_votes + 1
    
    
    # A complete list of candidates who received votes and total number of votes each candidates won
    candidate_name = row[2]
    total_candidates_votes[candidate_name] = total_candidates_votes.get(candidate_name,0) + 1
    
#The winner of the election based on popular vote.
candidates = list(total_candidates_votes.keys())
votes = list(total_candidates_votes.values())
max_votes = max(votes)

index = votes.index(max_votes)
winner_candidate = candidates[index]

#Showing output in terminal
print("Election Results")
print("----------------------------")
print(f"Total Voters: {total_votes}")
print("----------------------------")
for candidate_name in total_candidates_votes:
    votes = total_candidates_votes[candidate_name]
    votes_pct = str(round(votes/total_votes*100,3))+"%"
    print(f"{candidate_name}: {votes_pct} ({votes})")
    
    
print("----------------------------")
print(f"Winner: {winner_candidate}")
print("----------------------------")   

poll_output = os.path.join(os.getcwd(),"analysis","poll_analysis.txt")

#creating text file with the output
with open(poll_output,'w') as out:
    out.write("Election Results\n")
    out.write("----------------------------\n")
    out.write(f"Total Voters: {total_votes}\n")
    out.write("----------------------------\n")
    for candidate_name in total_candidates_votes:
        votes = total_candidates_votes[candidate_name]
        votes_pct = str(round(votes/total_votes*100,3))+"%"
        out.write(f"{candidate_name}: {votes_pct} ({votes})\n")
    out.write("----------------------------\n")
    out.write(f"Winner: {winner_candidate}\n")
    out.write("----------------------------\n")   