##### PyBank Challenge #####

### * The total number of months included in the dataset

# Open dataset and read dataset
with open('budget_data.csv', 'r') as f:
    contents = f.read()
print(contents)

#     rows = contents.split('\n')

#     # Remove any empty rows
#     rows = [row for row in rows if row]

#     # Subtract 1 from the number of rows to account for the header row
#     num_months = len(rows) - 1

# # Print t    # Split the contents into rows using newline as the delimiter
# he result
# print("Total number of months: ", num_months)
