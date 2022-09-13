# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options list []
candidate_options = []

# Candidate votes dictionary
candidate_votes = {}

# Wining Candiate and Winning Count Tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

# Open the election results and read the file
# encoding was cp1252, added ", encoding='utf-8'" to match lesson
with open(file_to_load, encoding='utf-8') as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # can augment to total_votes += 1, but just getting used to below format
        total_votes = total_votes + 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # if candidate name has been added to list then dont add again
        if candidate_name not in candidate_options:
          
          # Add the candidate name to the candidate list
          candidate_options.append(candidate_name)

          # track candidate's vote count. Votes start at 0
          candidate_votes[candidate_name] = 0

        # Increment vote count by 1
        # Place inside for loop and outside if statement
        candidate_votes[candidate_name] +=1

# save results to txt file
with open(file_to_save, "w") as txt_file:
  election_results=(
    f'\nElection Results\n'
    f'-------------------------\n'
    f'Total Votes: {total_votes:,}\n'
    f'-------------------------\n')
  print(election_results, end="")
  #Save the finel vore count to the text file
  txt_file.write(election_results)
  
      #Determine the percentage of the votes for each candidate by looping through counts
      # Iterate through the candidate list
  for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) *100
        
        #To do: print out each candidate's name, vote count, and percentage of
        # voted to the terminal
        candidate_results = (
          f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        print(candidate_results)

        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
          # if true then set winning_count = votes
          # and winning_percentage = vote_percentage
          winning_count = votes
          winning_percentage = vote_percentage
          # set winning_candidate = candidate_name
          winning_candidate = candidate_name

  #To do: print out the winning candidate, votecount and
  # and percentage to terminal
  winning_candidate_summary = (f'-------------------------\n'
      f'Winner: {winning_candidate}\n'
      f'Wining Vote Count: {winning_count:,}\n'
      f'Winning Percentage: {winning_percentage:.1f}%\n'
      f'-------------------------\n')
  print(winning_candidate_summary)
  # Save the tinning candidate's results to tthe text file.
  txt_file.write(winning_candidate_summary)

