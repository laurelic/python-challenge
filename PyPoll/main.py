
#challenge: to parse through a csv and summarize the data using only built in functions

#load pre-requisites
import csv
import os

#specify the path
path = os.path.join('Resources', 'election_data.csv')

#import the csv file
with open(path, newline='') as poll_raw:
    poll_read = csv.reader(poll_raw, delimiter=",")
    
    #determine the heaer row
    poll_head = next(poll_read)
    
    #generate a list of the canditates
    c_list = [row[2] for row in poll_read]
    
    #use len to get the total vote count
    vote_count = len(c_list)
    
    #iterate over the list to create a dictionary of unique keys and counters
    poll_counts = {}
    for i in c_list:
        if i in poll_counts:
            poll_counts[i] +=1
        else:
            poll_counts[i] = 1
    
    #print summary to screen
    print('Election Results')
    print('\n-------------------------')
    print('\nTotal Votes: ' + str(vote_count))
    print('\n-------------------------')

#iterate through dictionary to print candidate's name, calculate percentage of votes, and determine winner
win_val = 0
for key in poll_counts.keys():
    if poll_counts[key] > win_val:
        win_val = poll_counts[key]
    print(key + ": " + str(round((poll_counts[key]/vote_count)*100, 3)) + "% (" + str(poll_counts[key]) + ")")

win_name = [key for key, value in poll_counts.items() if value == win_val][0]
print('\n-------------------------')
print('\nWinner: ' + win_name)
print('\n-------------------------')
  
#write all the findings in a text file
poll_text = open("PyPoll-output.txt", "w")
poll_text.write('Election Results')
poll_text.write('\n-------------------------')
poll_text.write('\nTotal Votes: ' + str(vote_count))
poll_text.write('\n-------------------------')
for key in poll_counts.keys():
    poll_text.write("\n" + key + ": " + str(round((poll_counts[key]/vote_count)*100, 3)) + "% (" + str(poll_counts[key]) + ")")
poll_text.write('\n-------------------------')
poll_text.write('\nWinner: ' + win_name)
poll_text.write('\n-------------------------')
poll_text.close()

