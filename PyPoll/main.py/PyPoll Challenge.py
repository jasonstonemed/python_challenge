##### PyPoll Challenge #####

# variables

totalVotes = 0

# Prepare data
import csv
with open('election_data.csv', 'r') as file:
    firstRow = csv.reader(file)
    next(firstRow) #loop starting point  

    for i in firstRow:    
        totalVotes += 1

print(f"Total Votes Counted:{totalVotes}")




#Total votes counted loop



