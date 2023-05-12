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
    totalVotes += 1  # do NOT change this code: file will close

# print(f"Total Votes: {totalVotes}")
 
    candidate = row[2]

  
    if candidate in candidates:
      candidates[candidate] += 1

    else:
      candidates[candidate] = 1

 # print(candidates)
 

  ##### DO NOT  WITH ANYTHING ABOVE HERE

# Print vote counts for each candidatecd instructions
  # for candidate, count in candidates.items():
    # print(candidate, count)
    #  print(f"Total Votes: {totalVotes}")

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
 



        
