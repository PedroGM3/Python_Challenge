#create dependencies

import os
import csv


# Path for resource file

bank_csv = os.path.join( "Resources", "budget_data.csv")

# Create lists to store information

months = []
profit = []
change =[]
change_per = []

#open csv and populate the lists with data
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)

    for row in csvreader:

        # add month
        months.append(row[0])

        # Add profit
        profit.append(row[1])

# loop to calculate the total
total = 0
for i in profit:
    total = float(i) + total

# number of months
month_count = len(months)

# add change
change.append(0)
for j in range(1,month_count):
    change.append(float(profit[j]) - float(profit[j-1]))

# calculate average change

totalchange = 0
for i in change:
    totalchange = float(i) + totalchange


avg_change = totalchange / (month_count -1)

# identify min and max values

maxinc = max(change)
maxdec = min(change)

maxindex = change.index(maxinc)
minindex = change.index(maxdec)

maxdate = months[maxindex]
mindate = months[minindex]



#print data

analysis_out =("Financial Analysis\n"
"____________________________\n"
f"Total months: {month_count}\n"
f"Total: ${total}\n"
f"Average Change: ${avg_change}\n"
f"Greatest increase in profits: {maxdate} : ${maxinc}\n"
f"Greatest decrease in profits: {mindate} : ${maxdec}\n")


print(analysis_out)


# create txt file

results = os.path.join("Analysis","PyBank_Analysis.txt")

with open(results, "w") as textfile:
    textfile.write(analysis_out)

