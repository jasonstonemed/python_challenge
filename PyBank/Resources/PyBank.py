##### PyBank Challenge #####

# import modules
import csv
import os

# set path
csv_file = os.path.join("budget_data.csv")
                     
# initialize

total_months = 0

#  open file, skip header, count months
with open('budget_data.csv') as file:
    reader = csv.reader(file) # converts csv to strings - establishes column header row
    next(reader)  # skip header row

    #total number of months in data
    total_months += 1

    # print(f'The number of months in the file is: {total_months}')ls


##### The net total amount of "Profit/Losses" over {months} #####

#prepare data
import csv

#open and set loop
with open('budget_data.csv', 'r') as file:
    reader = csv.DictReader(file) #applying DictReader
    total_profit_loss = 0 # starting point
    for row in reader: # identify loop type
        total_profit_loss += int(row['Profit/Losses']) # adds cell values for each row through the loop

print(f'The net total amount of "Profit/Losses" over {total_months} months is: ${total_profit_loss}')

##### The changes in "Profit/Losses" over the entire period, and then the average of those changes

# Prepare data
import csv

with open('budget_data.csv', 'r') as file: #open and set loop
    reader = csv.DictReader(file) # header row
    first_row = next(reader)  # skips the first row
    previous_profit_loss = int(first_row['Profit/Losses']) # converts first row to numbers
    total_change = 0 # starting pt for total change
    num_changes = 0 #starting pt for num changes
    for row in reader:
        current_profit_loss = int(row['Profit/Losses']) #changes rows to an integer for counting
        change = current_profit_loss - previous_profit_loss #defines change variable
        total_change += change #counting mechanism
        num_changes += 1 #counting mechanism
        previous_profit_loss = current_profit_loss #starts loop again

#calculate average daily change
average_change = total_change / num_changes #sets variable

# print(f'The changes in "Profit/Losses" over {total_months} months is: ${total_change}')
# print(f'The average of those changes is: ${average_change:.2f}')



##### The greatest increase in profits (date and amount) over the entire period #####

import csv

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #takes out commas from data
    next(csvreader)  # skip header row

    # Set variables
    total_months = 0
    total_profit = 0
    previous_profit = 0
    greatest_profit_increase = 0
    greatest_profit_increase_month = "" #sets empty string variable

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

            # Check if the current profit increase is the greatest so far
            if profit_change > greatest_profit_increase:
                greatest_profit_increase = profit_change
                greatest_profit_increase_month = month

        # Update the previous profit for the next iteration
        previous_profit = profit

    

##### greatest decrease in profits (date and amount) over the entire period #####

import csv

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

            print(greatest_profit_increase_month)

        

        # Update the previous profit for the next iteration
        previous_profit = profit

        

    # Print the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profit: ${total_profit}")
    print(f"Average Change: ${round((total_profit-previous_profit)/(total_months-1),2)}")
    print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})")
    print(f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})")


 