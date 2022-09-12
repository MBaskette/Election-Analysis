# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
# encoding was cp1252 added ", encoding='utf-8'" to match lesson
with open(file_to_load, encoding='utf-8') as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
# 1. The total number of votes cast
# 2. Complete list of candidates that recieved votes
# 3. Total votes for each candidate
# 4. The percentage of votes cast for each candidate
# 5. Winner based off of the popular vote

# Create a filename variable to a direct or indirect path to the file.

# Using the open statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:
# write some data to the file.
  #  txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


