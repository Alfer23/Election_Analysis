#The data we need to retrieve

#1. The total number of votes cast

#2. A complete list of candidates who received votes

#3. The percentages of votes each candidate won

#4. The total number of votes each candidate won

#5. The winner of the election based on popular vote
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. Initialize a total vote counter
total_votes=0
#Declare an empty list
candidate_options=[]
#Declare an empty  dictionary
candidate_votes={}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader=csv.reader(election_data)

    #Print the header row
    headers=next(file_reader)

    #print(headers)

    #Print each row in the CSV file
    for row in file_reader:
        #print(row)

        #2. Add to the total vote count
        total_votes+=1

        #Print the candidate name from each row
        candidate_name=row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add the candidate name to the list
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count
            candidate_votes[candidate_name]=0
#When we add candidate_votes[candidate_name] = 0, we're setting each candidate's vote count to zero.
# Once we set it to zero, then we can start tallying the votes for each candidate.
        candidate_votes[candidate_name]+=1
#To begin tracking the candidate's vote count, we initializing each candidate's vote equal to zero.
# Next, we need to increment the votes by 1 every time a candidate name appears in a row.
# Incrementing the votes for each candidate inside the if statement will increment the candidate's vote by only 1 every time we run the file.
        #Determine the percentage of votes for each candidate by looping through the counts
        #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage=float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes
        print(f"{candidate_name}:received{vote_percentage:.1f}% of the vote.")


#3.Print the total votes
#print(candidate_votes)


