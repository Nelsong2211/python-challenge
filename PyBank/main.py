import os
import csv

PyBank_csv = os.path.join("Resources", "02-Homework_03-Python_PyBank_Resources_budget_data.csv")

months= []
totalNetChange = []
totalmonths = 0
totalNet = 0

biggestNum = 0
biggestMonth = ""
smallestNum = 0
smallestMonth = ""


with open(PyBank_csv, "r") as Bank_file:
    csvreader = csv.reader(Bank_file, delimiter=",")
    header_row = next(csvreader)

    first_row = next(csvreader)
    prevNet = int(first_row[1])
    

    for row in csvreader:
        netChange = int(row[1]) - prevNet
        prevNet = int(row[1])
       
        months.append(row[0])
        totalNetChange.append(netChange)


       
        totalmonths= totalmonths + 1
        
        totalNet = int(first_row[1])

        if netChange > biggestNum:
            biggestMonth = row[0]
            biggestNum = netChange

        if netChange < smallestNum:
            smallestMonth = row[0]
            smallestNum = netChange


print( "Total Months: " + str(totalmonths))
print( "Total Revenue: " + "$" +str(totalNet))
print("Biggest increase happend on "  + biggestMonth + " and was " + "$" + str(biggestNum))
print("Biggest decrease happend on "  + smallestMonth + " and was " + "$" + str(smallestNum))

with open("analysis.txt", "a") as f:
    print( "Total Months: " + str(totalmonths), file=f)
    print( "Total Revenue: " + "$" +str(totalNet), file=f)
    print("Biggest increase happend on "  + biggestMonth + " and was " + "$" + str(biggestNum), file=f)
    print("Biggest decrease happend on "  + smallestMonth + " and was " + "$" + str(smallestNum), file=f)
