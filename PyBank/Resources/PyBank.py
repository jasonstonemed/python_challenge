##### PyBank Challenge #####

# import modules
import csv
import os

# set path
csv_file = os.path.join("budget_data.csv")
                     
# initialize months
total_months = 0

#  open file, skip header, count months
with open(csv_file,'r') as file:
    reader = csv.reader(file) 
    next(reader)  

    #total number of months in data
    for i in reader:
        total_months += 1

##### The net total amount of "Profit/Losses" over {months} #####

#open and set loop
with open('budget_data.csv', 'r') as file:
    reader = csv.DictReader(file) 
    
    #initialize
    total_profit_loss = 0 
    for row in reader:
        total_profit_loss += int(row['Profit/Losses']) 

##### The changes in "Profit/Losses" over the entire period, and then the average of those changes

# Prepare data
import csv

with open('budget_data.csv', 'r') as file: 
    reader = csv.DictReader(file) 
    first_row = next(reader) 

    #initialize
    previous_profit_loss = int(first_row['Profit/Losses']) 
    total_change = 0 

    for row in reader:
        #set current month
        current_profit_loss = int(row['Profit/Losses'])     

        #calculate change from previous month
        change = current_profit_loss - previous_profit_loss 

        #update total change and number of changes
        total_change += change 

        #update previous profit for nect iteration
        previous_profit_loss = current_profit_loss 

        #calculate average daily change
        average_change = total_change / total_months

##### The greatest increase in profits (date and amount) over the entire period #####

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    next(csvreader) 

    # Set variables
    total_months = 0
    total_profit = 0
    previous_profit = 0
    greatest_profit_increase = 0
    greatest_profit_increase_month = "" 

    for row in csvreader:
        # Extract the month and profit/loss from the current row
        month = row[0]
        profit = int(row[1])

        # Update the total number of months and total profit
        total_months += 1
        total_profit += profit

        # Calculate the change in profit from the previous month
        if total_months > 1:
            profit_change = profit - previous_profit

            # Check if the current profit increase is the greatest so far
            if profit_change > greatest_profit_increase:
                greatest_profit_increase = profit_change
                greatest_profit_increase_month = month

        # Update the previous profit for the next iteration
        previous_profit = profit    

##### greatest decrease in profits (date and amount) over the entire period #####

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # skip header row

    # Initialize variables
    total_months = 0
    total_profit = 0
    previous_profit = 0
    greatest_profit_decrease = 0
    greatest_profit_increase = 0
    greatest_profit_decrease_month = ""
    greatest_profit_increase_month = ""

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract the month and profit/loss from the current row
        month = row[0]
        profit = int(row[1])

        # Update the total number of months and total profit
        total_months += 1
        total_profit += profit

        # Calculate the change in profit from the previous month
        if total_months > 1:
            profit_change = profit - previous_profit

            # Check if the current profit decrease is the greatest so far
            if profit_change < greatest_profit_decrease:
                greatest_profit_decrease = profit_change
                greatest_profit_decrease_month = month
            elif profit_change > greatest_profit_increase:
                greatest_profit_increase = profit_change
                greatest_profit_increase_month = month

        # Update the previous profit for the next iteration
        previous_profit = profit        

    # Print the results
    print("------------------")
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profit: ${total_profit}")
    print(f'Average change in Profit/Losses over {total_months} months is: ${round((average_change))}')
    print(f"Greatest Increase in Profits: {greatest_profit_increase_month} ${greatest_profit_increase}")
    print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} ${greatest_profit_decrease}")
    print("------------------")


 
