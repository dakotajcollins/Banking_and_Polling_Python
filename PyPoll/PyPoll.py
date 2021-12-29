f= open("Pypoll_Results.txt","w")

print("Election Results",file=open("Pypoll_Results.txt","a"))
print("Election Results")

print("-------------------------",file=open("Pypoll_Results.txt","a"))
print("-------------------------")

import os
import csv
poll_csv="Resources/election_data.csv"
with open(poll_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    next(csv_reader) #skip the header

    #Find total votes
    total_votes=len(list(csv_reader))
    print(f'Total Votes: {total_votes}',file=open("Pypoll_Results.txt","a"))
    print(f'Total Votes: {total_votes}')

    print('-------------------------',file=open("Pypoll_Results.txt","a"))
    print('-------------------------')




khan_vote=0
correy_vote=0
li_vote=0
ot_vote=0

with open(poll_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")


    new_list=[]
    
    for row in csv_reader:
        new_list.append(row)

# find values
    for row in new_list:

        if row[2] == "Khan":
            khan_vote = khan_vote +1
        elif row[2] == "Correy":
            correy_vote = correy_vote +1
        elif row[2] == "Li":
            li_vote = li_vote+1
        elif row[2] == "O'Tooley":
            ot_vote = ot_vote+1


# Kahn stats
khan_percent= round((khan_vote/total_votes)*100,3)
print(f'Khan: {khan_percent}% ({khan_vote})',file=open("Pypoll_Results.txt","a"))
print(f'Khan: {khan_percent}% ({khan_vote})')


#Correy stats


correy_percent= round((correy_vote/total_votes)*100,3)
print(f'Correy: {correy_percent}% ({correy_vote})',file=open("Pypoll_Results.txt","a"))
print(f'Correy: {correy_percent}% ({correy_vote})')



#Li stats

li_percent= round((li_vote/total_votes)*100,3)
print(f'Li: {li_percent}% ({li_vote})',file=open("Pypoll_Results.txt","a"))
print(f'Li: {li_percent}% ({li_vote})')


#O'Tooley stats

ot_percent= round((ot_vote/total_votes)*100,3)
print(f"O'Tooley: {ot_percent}% ({ot_vote})",file=open("Pypoll_Results.txt","a"))

print('-------------------------',file=open("Pypoll_Results.txt","a"))
print('-------------------------')


#Find the winner
name=["Khan","Correy","Li","O'Tooley"]
votes=[khan_vote,correy_vote,li_vote,ot_vote]
tally=0
for i in votes:
    if i > tally:
        tally=i
winner_index=votes.index(tally)
winner=name[winner_index]   
print(f'Winner: {winner}',file=open("Pypoll_Results.txt","a"))
print(f'Winner: {winner}')



print("-------------------------",file=open("Pypoll_Results.txt","a"))
print("-------------------------")
