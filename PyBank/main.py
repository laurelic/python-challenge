#challenge: to parse and analyze a csv using only built-in python functions (no pandas)

#import the csv and os dependencies
import os
import csv

#specify the path
path = os.path.join('Resources', 'budget_data.csv')

#import the csv file
with open(path, newline='') as bud_raw:
    bud_read = csv.reader(bud_raw, delimiter=',')
    
    #determine the header row
    bud_head = next(bud_read)
    
    #declare the variables to be filled by a single for loop
    month_count = 0 
    pl_sum = 0 
    pl_list = []
    date_list = []
    
    #create distinct lists for each data type so that they may be iterated over multiple times
    for row in bud_read:
        month_count +=1
        pl_sum += int(row[1])
        pl_list.append(int(row[1]))
        date_list.append(row[0])
      
    #iterate over the profit/loss list to determine the difference between each item
    #and store in a new list
    change_list = [0,]
    i = 1
    while i < len(pl_list):
        change_val = int(pl_list[i]) - int(pl_list[i-1])
        change_list.append(change_val)
        i+=1
    
    #sum the list of changes and divide by its length to determine average change
    pl_avg_change = round(sum(change_list)/(len(change_list)-1),2)
    
    #determine the maximum and minimum changes in the list
    max_change = max(change_list)
    min_change = min(change_list)
    
    #zip the changes and corresponding dates into a dictionary
    change_zip = dict(zip(change_list, date_list))
    
    #Print all the findings in a summary
    print('Financial Analysis \n----------------------------')
    print('Total Months: ' + str(month_count))
    print('Total: $' + str(pl_sum))
    print('Average Change: $' + str(pl_avg_change))
    print('Greatest Increase in Profits: ' + change_zip[max_change] + ' ($' + str(max_change) + ')')
    print('Greatest Decrease in Profits: ' + change_zip[min_change] + ' ($' + str(min_change) + ')')

#write all the findings in a text file
pb_text = open("PyBank-output.txt", "w")
    pb_text.write('Financial Analysis \n----------------------------')
    pb_text.write('\nTotal Months: ' + str(month_count))
    pb_text.write('\nTotal: $' + str(pl_sum))
    pb_text.write('\nAverage Change: $' + str(pl_avg_change))
    pb_text.write('\nGreatest Increase in Profits: ' + change_zip[max_change] + ' ($' + str(max_change) + ')')
    pb_text.write('\nGreatest Decrease in Profits: ' + change_zip[min_change] + ' ($' + str(min_change) + ')')
    pb_text.close()

