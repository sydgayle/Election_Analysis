#the data we need to retrieve
#Total Number of votes Cast
#list of candidates
#votes for each candidate
#%each won
#winner based on votes

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.

# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
 #    print(election_data)

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#1Setting Total Votes to 0
total_votes = 0
#setting the total county votes

# Candidate Options
candidate_options = []
#county list
county_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}
#county dictionary
county_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#winning county
winning_county = ""
county_winning_count = 0
county_winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   
    # Print the header row.
    headers = next(file_reader)
  
# Using the with statement open the file as a text file.

# Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
# Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
             # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
             # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        #county code
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if county_name not in county_options:
            # Add it to the list of candidates.
            county_options.append(county_name)
             # 2. Begin tracking that candidate's vote count. 
            county_votes[county_name] = 0
             # Add a vote to that candidate's count.
        county_votes[county_name] += 1
    
     # Determine winning vote count and candidate
    with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"\n"
            f"County Votes:\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        
          
         # Calculate county vote percentage
        for county in county_votes:
            # 2. Retrieve vote count of a candidate.
            votes = county_votes[county]

            # 3. Calculate the percentage of votes.
            county_vote_percentage = float(votes) / float(total_votes) * 100
            county_vote_results = (f"{county}: {county_vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            # Print each candidate, their voter count, and percentage to the terminal.
                      
            print(county_vote_results)
            #  Save the candidate results to our text file.
            txt_file.write(county_vote_results)
        
            if (votes > county_winning_count) and (county_vote_percentage > county_winning_percentage):
                    # 2. If true then set winning_count = votes and winning_percent =
                    # vote_percentage.
                county_winning_count = votes
                county_winning_percentage = county_vote_percentage
                    # 3. Set the winning_candidate equal to the candidate's name.
                winning_county = county        
        winning_county_summary = (
                        f"-------------------------\n"
                        f"Largest County Turnout: {winning_county}\n"
                        f"-------------------------\n")
        print(winning_county_summary)
        txt_file.write(winning_county_summary)

          # Determine the percentage of votes for each candidate by looping through the counts.
            # 1. Iterate through the candidate list.
        for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
        
        # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100


    # Print each candidate, their voter count, and percentage to the
    # terminal.
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
  # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
#  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                        # 2. If true then set winning_count = votes and winning_percent =
                        # vote_percentage.
                    winning_count = votes
                    winning_percentage = vote_percentage
                        # 3. Set the winning_candidate equal to the candidate's name.
                    winning_candidate = candidate 
       

        winning_candidate_summary = (
                        f"-------------------------\n"
                        f"Winner: {winning_candidate}\n"
                        f"Winning Vote Count: {winning_count:,}\n"
                        f"Winning Percentage: {winning_percentage:.1f}%\n"
                        f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file.
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)
    
        
    # 3. Print the total votes.
    #print(candidate_options)
    #print(total_votes)
    #print(candidate_votes)
    #print(winning_candidate)
    #with open(file_to_save, "w") as txt_file:


    #   txt_file.write("Counties in the Election")
    #  txt_file.write("\n-------------------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")


    # Create a filename variable to a direct or indirect path to the file.
    #file_to_save = os.path.join("Analysis", "election_analysis.txt")

    # Using the with statement open the file as a text file.
    #with open(file_to_save, "w") as txt_file:

        # Write some data to the file.
        #txt_file.write("Hello World")
        # Write three counties to the file.
   
