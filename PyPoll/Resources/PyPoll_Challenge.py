# PyPoll Challenge 

##### Total Votes counted
# import modules
import csv
import os
print(os.getcwd())
# set path
csv_file = os.path.join("election_data.csv")

# initialize  

totalVotes = 0  
candidates = {}
count = 0  
votes = 0 


# open with reader module and set resources
with open(csv_file,'r') as file:        
  reader = csv.reader(file)
  next(reader) #loop starting point ls

# Total number of votes
  for row in reader:  
    totalVotes += 1  
  print(f"Total Votes: {totalVotes}")
  
 # Tally votes for each candidate
    # initialize
    candidate = row[2]

    if candidate in candidates:
      candidates[candidate] += 1

    else:
      candidates[candidate] = 1

   print(candidates) 

  print("Election Results")
  print("-------------------------")
  print(f"Total Votes: {totalVotes}")
  print("-------------------------")

# Calculate percentage of votes for each candidate and print results
  for candidate, count in candidates.items():
    percent_of_vote = count/totalVotes * 100
    print(f"{candidate}: {percent_of_vote:.2f}% ({count})")

# Determine the winner and print result

  winner = max(candidates, key=candidates.get)

  print("-------------------------")
  print(f"Winner: {winner}")
  print("-------------------------")
 



        
