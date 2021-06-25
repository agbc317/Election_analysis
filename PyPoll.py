#Add dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a file name variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize total votes counter
total_votes = 0

#Declare new list of Candidate Names
candidate_options = []
#Declare empty dictionary of candidate votes
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:   
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #Get candidates name
        candidate_name = row[2]
        #Add candidate name to candidate options
        if candidate_name not in candidate_options:
            #Add candidate to list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking candidates votes
            candidate_votes[candidate_name] = 0
        #Add vote to candidates vote count
        candidate_votes[candidate_name] += 1

#Save results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file.
    txt_file.write(election_results)
    #Determine percentage of votes for each candidate
    #1. Iterate through candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate percentage of votes.
        vote_percentage = (float(votes) / float(total_votes)) * 100
        #4. print the candidate name and percentage of votes.
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        #Print each candidates results
        print(candidate_results)
            #Save candidates results to text file.
        txt_file.write(candidate_results)

    #Determine winning vote count and candidate
    #1. Determine if the votes are greater than the winning count.    
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2. If true then set winning_count = votes and winning_percentage = vote_percentage
        #vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
        #and set winning candidate equal to candidate's name
            winning_candidate = candidate_name
    #Print the name, vote count, and vote percentage of the winning candidate
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidates name to the text file
    txt_file.write(winning_candidate_summary)

