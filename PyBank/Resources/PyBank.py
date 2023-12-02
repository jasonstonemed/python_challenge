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
<<<<<<< HEAD
    for i in reader:
        total_months += 1
=======
    total_months += 1

    # print(f'The number of months in the file is: {total_months}')

>>>>>>> da7a0c3a7422d796937e5d1ae05f78e8a107ef52

##### The net total amount of "Profit/Losses" over {months} #####

#open and set loop
with open('budget_data.csv', 'r') as file:
    reader = csv.DictReader(file) #applying DictReader uses string columns instead of indices
    total_profit_loss = 0 
    for row in reader:
        total_profit_loss += int(row['Profit/Losses']) 

print(f'The net total amount of "Profit/Losses" over {total_months} months is: ${total_profit_loss}')

##### The changes in "Profit/Losses" over the entire period, and then the average of those changes

<<<<<<< HEAD
# Prepare data
import csv

with open('budget_data.csv', 'r') as file: 
    reader = csv.DictReader(file) 
    first_row = next(reader) 
    #initialize
    previous_profit_loss = int(first_row['Profit/Losses']) 
    total_change = 0 
    # num_changes = 0 

=======
with open('budget_data.csv', 'r') as file: #open and set loop
    reader = csv.DictReader(file) # header row
    first_row = next(reader)  # skips the first row
    previous_profit_loss = int(first_row['Profit/Losses']) # converts first row to numbers
    total_change = 0 # starting pt for total change
    num_changes = 0 #starting pt for num changes
>>>>>>> da7a0c3a7422d796937e5d1ae05f78e8a107ef52
    for row in reader:
        current_profit_loss = int(row['Profit/Losses']) 

        #calculate change from previous month
        change = current_profit_loss - previous_profit_loss

        #update total change and number of changes
        total_change += change
        # num_changes += 1

        #update previous profit for nect iteration
        previous_profit_loss = current_profit_loss

#calculate average daily change
average_change = total_change / total_months
# num_changes
print(f'The average change in "Profit/Losses" over {total_months} months is: ${average_change}')
    

<<<<<<< HEAD
#         #calculate change from previous month
#         change = current_profit_loss - previous_profit_loss 

#         #update total change and number of changes
#         total_change += change 
#         num_changes += 1 

#         #update previous profit for nect iteration
#         previous_profit_loss = current_profit_loss 
=======
print(f'The changes in "Profit/Losses" over {total_months} months is: ${total_change}')
print(f'The average of those changes is: ${average_change:.2f}')
>>>>>>> da7a0c3a7422d796937e5d1ae05f78e8a107ef52

# #calculate average daily change
# average_change = total_change / num_changes
# print(average_change)

# ##### The greatest increase in profits (date and amount) over the entire period #####

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    next(csvreader) 

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
    print(f'Average change in Profit/Losses over {total_months} months is: ${round((average_change), 2)}')
    print(f"Greatest Increase in Profits: {greatest_profit_increase_month} ${greatest_profit_increase}")
    print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} ${greatest_profit_decrease}")


 
