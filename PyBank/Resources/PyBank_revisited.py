#### PyBank Challenge - Revisited ####

# 1. The net total amount of "Profit/Losses" over {months}
# 2. The changes in "Profit/Losses" over the entire period, 
# and then the average of those changes
# 3. The greatest increase in profits (date and amount) over the period
# 4. The greatest decrease in profits (date and amount) over the period

# import modules
import csv
import os


# set path
csv_file = os.path.join("budget_data.csv")
                     
# initialize variables
total_months = 0
total_profit_loss = 0
total_change = 0
previous_profit_loss = None
greatest_profit_increase = 0
greatest_profit_increase_mo = ""
greatest_profit_decrease = 0 
greatest_profit_decrease_mo = ""

#  open file, skip header, count months
with open(csv_file, 'r') as file:
    reader = csv.reader(file) 
    next(reader)  

    for row in reader:

    # Count months
        total_months +=1

    # Net total of profits
        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss

    # The changes in "Profit/Losses" over the entire period, 
    # and then the average of those changes

        #Calculate change from previous month
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            total_change += change
        
        # Check if the current profit increase is the greatest so far
            if change > greatest_profit_increase:
                greatest_profit_increase = change
                greatest_profit_increase_mo = row[0]
            elif change < greatest_profit_decrease:
                greatest_profit_decrease = change
                greatest_profit_decrease_mo = row[0]

        # Update previous profit
        previous_profit_loss = current_profit_loss

    #Average of the changes
    if total_months > 1:
        average_change = total_change / total_months
       
    # Print the results
    print("------------------")
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profit: ${total_profit_loss}")
    print(f'Average change in Profit/Losses over {total_months} months is: ${round((average_change))}')
    print(f"Greatest Increase in Profits: {greatest_profit_increase_mo} ${greatest_profit_increase}")
    print(f"Greatest Decrease in Profits: {greatest_profit_decrease_mo} ${greatest_profit_decrease}")
    print("------------------")


