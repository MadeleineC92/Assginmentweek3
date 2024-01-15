#import modules

import os
import csv


#set file path 

csv_path =os.path.join("RESOURCES","budget_data.csv")

#variables 
Date=[]
Profit_Losses=[]
Monthly_changes=[]
Prev_profit=0    

#open file
with open(csv_path,'r') as csvdata:

    reader = csv.reader(csvdata)
    header = next(reader)
    
 #create loop for data     
    for row in reader:
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))
        if len(Date) == 1:
            Monthly_changes.append(0)
        else:
            current_change = int(row[1])-Prev_profit
            Monthly_changes.append(current_change)
        Prev_profit = int(row[1])

        
#caculations   
#len will count
total_months =len(Date)

Average =sum(Monthly_changes)/(total_months-1)

Total_profit =sum(Profit_Losses)

increase = max(Monthly_changes)

decrease = min(Monthly_changes)

date_increase = Date[Monthly_changes.index(increase)]
date_decrease = Date[Monthly_changes.index(decrease)]

#print to terminal  
#need to make values into string to show

print("Financial Analysis")
print("-----------------")
print("Total Months: " + str(total_months))
print("Total: " + str('${:,.0f}'.format(Total_profit)))
print("-----------------")
print("Average Change:" + str('${:,.2f}'.format(Average)))
print("Greates increase in profits: " + str(date_increase)+"     " + str('${:,.0f}'.format(increase)))
print("Greates decrease in profits: " + str(date_decrease)+"     " + str('${:,.0f}'.format(decrease)))       

#export text file 
with open('ANALYSIS/Financial.txt','w') as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${Total_profit:,.0f}\n")
    text.write("-------------------------\n")
    text.write(f"Average Change: {Average:,.2f}\n")
    text.write(f"Greates increase in profits: {date_increase} (${increase:,.0f})\n")
    text.write(f"Greates decrease in profits: {date_decrease} (${decrease:,.0f})\n")