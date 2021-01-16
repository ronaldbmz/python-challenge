#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:45:41 2021

@author: ron manipol
"""

import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join("02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")


#Variables
total_months = 0
net_total_amount = 0
greatest_increase_profit = None
greatest_decrease_profit = None

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    
     # Loop through the data
    for row in csvreader: #['01-2010','10,000']
        #The total number of months included in the dataset
        total_months = total_months + 1 
        
        #The net total amount of "Profit/Losses" over the entire period
        net_total_amount = net_total_amount + int(row[1])
        
        #The greatest increase in profits (date and amount) over the entire period
        if greatest_increase_profit==None:
            greatest_increase_profit = int(row[1])
            greatest_increase_month = row[0]
        elif greatest_increase_profit <int(row[1]):
            greatest_increase_profit = int(row[1])
            greatest_increase_month = row[0]
            
        #The greatest decrease in losses (date and amount) over the entire period
        if greatest_decrease_profit==None:
            greatest_decrease_profit = int(row[1])
            greatest_decrease_month = row[0]
        elif greatest_decrease_profit >int(row[1]):
            greatest_decrease_profit = int(row[1])
            greatest_decrease_month = row[0]
            
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
average_change = net_total_amount/total_months


# Showing output in Terminal
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})")



      
            
            

            
            

            
            
            
            
            
       