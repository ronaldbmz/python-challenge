#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:58:54 2021

@author: ron manipol
"""
import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join("..", "Resources",'02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')


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
    