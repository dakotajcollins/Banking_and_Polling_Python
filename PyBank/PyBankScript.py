f= open("PyBank_Results.txt","w")

print("Financial Analysis")
print("Financial Analysis",file=open("PyBank_Results.txt","a"))

print('----------------------------')
print('----------------------------',file=open("PyBank_Results.txt","a"))

import os
import csv
budget_csv = "Resources/budget_data.csv"

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader) #skip the header
    
#Find the total months    
    total_months=len(list(csv_reader))
    print(f"Total Months: {total_months}")
    print(f"Total Months: {total_months}",file=open("PyBank_Results.txt","a"))


with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)
    profit_list=[]

#Find the Net Profit
    for row in csv_reader:
        profit_list.append(float(row[1]))
    print(f'Net Profit/Loss: ${round(sum(profit_list))}')
    print(f'Net Profit/Loss: ${round(sum(profit_list))}',file=open("PyBank_Results.txt","a"))


# Find the average change    
    index=1
    average_change_list=[]
    
    while index < len(profit_list):
        average_change_list.append(profit_list[index]-profit_list[index-1])
        index=index+1

    def average():
        return sum(average_change_list)/len(average_change_list)
    print(f'Average Change: ${round(average(),2)}')
    print(f'Average Change: ${round(average(),2)}',file=open("PyBank_Results.txt","a"))


#Find the max and min index
    number=average_change_list
    max_check=max(number)
    min_check=min(number)
    i=number.index(max_check)
    j=number.index(min_check)


with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header=next(csv_reader)
    new_list=[]
    
    for row in csv_reader:
        new_list.append(row)

#Apply max and min index to the date in csv
max_date = new_list[i+1]
print(f'Greatest Increase in Profits: {max_date[0]} (${round(max_check)})')
print(f'Greatest Increase in Profits: {max_date[0]} (${round(max_check)})',file=open("PyBank_Results.txt","a"))

min_date = new_list[j+1]
print(f'Greatest Decrease in Profits: {min_date[0]} (${round(min_check)})')
print(f'Greatest Decrease in Profits: {min_date[0]} (${round(min_check)})',file=open("PyBank_Results.txt","a"))