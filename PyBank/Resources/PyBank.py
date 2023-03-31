##### PyBank Challenge #####

# The total number of months included in the dataset

# import modules
import csv
import os

# set path

csv_file = os.path.join("budget_data.csv")


# csv_file = os.path.join("budget_data.csv")
                        

# initialize

total_months = 0
net_profit = 0

#  open file, count months
with open('budget_data.csv') as file:
    reader = csv.reader(file) # converts csv to strings - establishes column header row
    next(reader)  # skip header row

    #total number of months in data
    for row in reader:                       
        total_months += 1 # Total number of votes 

# 
print(f'Total Months: {total_months}')


# ##### The net total amount of "Profit/Losses" over {months} #####

#open and set loop
with open('budget_data.csv', 'r') as file:
    reader = csv.DictReader(file) #applying DictReader
    for row in reader: 
        net_profit += int(row['Profit/Losses']) # adds cell values for each row through the loop

print(f'Net Profit/Loss: ${net_profit}')


##### The changes in "Profit/Losses" over the entire period, and then the average of those changes

#initialize 

day_one = 0 # starting pt for total change
next_day = 0
net_profit = 0


with open('budget_data.csv', 'r') as file: #open csv file
    reader = csv.DictReader(file) # header row
    next(reader)  # skips the first row 

    #net_profit over period

    net_profit += int(row["Profit/Losses"])
    
    new_profit = 0
    old_profit = 0
    total_change = 0
    current_profit = 0

# change in profits over period

    new_profit = int(row["Profit/Losses"])
    if total_months > 1:
        change = new_profit - old_profit
        total_change += change
        previous_profit = current_profit

        current_profit = int(row["Profit/Losses"])
        if total_months > 1:
            change = current_profit - previous_profit
            total_change += change
            previous_profit = current_profit
    
    
            for row in reader: #set loop
                day_one = (int(row['Profit/Losses'])) #changes rows to integers for counting
                next_day = (int(row['Profit/Losses']) + 1) 
                net_profit = ((day_one) - (next_day))

                (f"this is {net_profit}")

# average change over period

                average_change = total_change / (total_months - 1)

                print(f'Average Change: ${average_change:.2f}') ### this calculation is incorrect

# Month with greatest profit/loss

            # Initialize variables
            total_months = 0
            total_profit = 0
            previous_profit = 0
            greatest_profit_decrease = 0
            greatest_profit_decrease_month = ""

            # Loop through each row in the CSV file
            for row in reader:
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

                # Update the previous profit for the next iteration
                previous_profit = profit


       
        
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${net_profit}")
print(f"Average Change: ${round(total_change/(total_months-1),2)}")
print(f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_decrease})")









        
        

# #         print(daily_sum)


# #         # previous_profit_loss = int(first_row['Profit/Losses']) # converts first row to numbers
# #         # change = current_profit_loss - previous_profit_loss #defines change variable
# #         # total_change += change #counting mechanism
# # #         4

# # #     # Initialize variables
# # #     total_months = 0
# # #     total_profit = 0
# # #     previous_profit = 0
# # #     greatest_profit_decrease = 0
# # #     greatest_profit_decrease_month = ""

# # #     # Loop through each row in the CSV file
# # #     for row in csvreader:
# # #         # Extract the month and profit/loss from the current row
# # #         month = row[0]
# # #         profit = int(row[1])

# # #         # Update the total number of months and total profit
# # #         total_months += 1
# # #         total_profit += profit

# # #         # Calculate the change in profit from the previous month
# # #         if total_months > 1:
# # #             profit_change = profit - previous_profit

# # #             # Check if the current profit decrease is the greatest so far
# # #             if profit_change < greatest_profit_decrease:
# # #                 greatest_profit_decrease = profit_change
# # #                 greatest_profit_decrease_month = month

# # #         # Update the previous profit for the next iteration
# # #         previous_profit = profit

# # #     # Print the results
# # #     print("Financial Analysis")
# # #     print("------------------")
# # #     print(f"Total Months: {total_months}")
# # #     print(f"Total Profit: ${total_profit}")
# # #     print(f"Average Change: ${round((total_profit-previous_profit)/(total_months-1),2)}")
# # #     print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})")

 