##import modules - working
import os
import csv



#set file path -working
csv_path =os.path.join("resources","election_data.csv")



 #varabiles
candidate={}
count=0
winner={}

#open file   
with open(csv_path,'r') as csvdata:

        reader = csv.reader(csvdata)
        header = next(reader)
#if current_candidate on row 2 is in the candidate colume then add it together otherwise count it as 1 
#counting votes 
        for row in reader:
            #count 
            count = count+1 
            current_candidate= row[2]
    
            if current_candidate in candidate:
                candidate[current_candidate] += 1
            else:
                candidate[current_candidate] =1
                


                
#total sum
#if candidate = candidate then add to the next same candidate to get sepuarte count of each candidate
candidate["Charles Casper Stockham"] = (candidate["Charles Casper Stockham"])
vote_ccs =(candidate["Charles Casper Stockham"])

candidate["Diana DeGette"] = (candidate["Diana DeGette"])
vote_dd =(candidate["Diana DeGette"])

candidate["Raymon Anthony Doane"] = (candidate["Raymon Anthony Doane"])
vote_rad =(candidate["Raymon Anthony Doane"])


#percentage 
#total votes for indiv candidate / by total count * 100 to get percentage
ccs =(candidate["Charles Casper Stockham"])/(count)*100
dd =(candidate["Diana DeGette"])/(count)*100
rad =(candidate["Raymon Anthony Doane"])/(count)*100
                
#winner  - working              
inverse = [(value, key) for key, value in candidate.items()]
winner =(max(inverse)[1]) 

#printing termial -
#{:.3f}% ({})".format - this is how you format cells

print("Election Results")
print("-----------------")
print("Total Votes: " + str(count))
print("-----------------")
print("Charles Casper Stockham: {:.3f}% ({})".format(ccs, vote_ccs))
print("Diana DeGette: {:.3f}% ({})".format(dd, vote_dd))
print("Raymon Anthony Doane: {:.3f}% ({})".format(rad, vote_rad))
print("-----------------")
print("Winner:  " + str(winner))

#export text file 
with open('analysis/Election_Results.txt','w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {count}\n")
    text.write("-------------------------\n")
    text.write(f"Charles Casper Stockham: ({vote_ccs}) {ccs:,.3f}%\n")
    text.write(f"Diana DeGette: ({vote_dd}) {dd:,.3f}%\n")
    text.write(f"Raymon Anthony Doane: ({vote_rad}) {rad:,.3f}%\n")
    text.write(f'-----------------\n')
    text.write(f'Winner: {winner}\n')