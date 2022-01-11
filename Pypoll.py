import csv
import os


#file_to_load = 'Resources/election_results.csv'
#open and close file
#election_data=open(file_to_load,'r')

#election_data.close()
#with statement to open the file

file_to_load= os.path.join("Resources","election_results.csv")
files_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []

with open(file_to_load) as election_data:

    #read the file with reader function
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
   
    #print each row in the csv file
    for row in file_reader:
        total_votes +=1

        candidate_name =row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

print(total_votes)
print(candidate_options)



