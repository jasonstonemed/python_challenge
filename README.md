### PyPoll Challenge Readme

#### Overview:

The PyPoll Challenge is a Python script designed to analyze election data provided in a CSV file (`election_data.csv`). The script calculates and presents key election metrics, including the total number of votes, the percentage of votes for each candidate, and the winner of the election.

#### Requirements:

- Python 3.x
- `election_data.csv` file containing election data with columns "Voter ID," "County," and "Candidate."

#### Instructions:

1. **Download the Script:**
   - Download the Python script `pypoll_challenge.py` and save it in the same directory as your `election_data.csv` file.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script (`pypoll_challenge.py`) is saved.
   - Run the script by entering the command: `python pypoll_challenge.py`.

3. **View Results:**
   - The script will output the following election analysis results:
     - Total votes counted.
     - Percentage of votes for each candidate.
     - The winner of the election.

#### Example Output:

```plaintext
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.00% (2218231)
Correy: 20.00% (704200)
Li: 14.00% (492940)
O'Tooley: 3.00% (105630)
-------------------------
Winner: Khan
-------------------------
```

#### Notes:

- The script utilizes the `csv` and `os` modules to read the CSV file and handle file paths.
- Election metrics are calculated, including the total number of votes, the percentage of votes for each candidate, and the winner.
- The results are printed to the console for easy viewing.

#### Disclaimer:

This script assumes the input CSV file (`election_data.csv`) adheres to the specified format, and data is valid. Ensure that the file is present in the same directory as the script.

Readme assistance from ChatGPT
