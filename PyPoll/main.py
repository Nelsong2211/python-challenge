import os
import csv
PyPoll_csv = os.path.join("Resources", "02-Homework_03-Python_PyPoll_Resources_election_data.csv")

totalvotos= []
totalconuntry= []
totalcandidates= []
candidate= 0


with open(PyPoll_csv, "r") as Poll_file:
    csvreader = csv.reader(Poll_file, delimiter=",")
    header_row = next(csvreader)
    

    for row in csvreader:

        totalvotos.append(row[0])
        totalconuntry.append(row[1])
        totalcandidates.append(row[2])

       

        candidate= candidate + 1

Kant= totalcandidates.count("Khan")
Correy= totalcandidates.count("Correy")
Li= totalcandidates.count("Li")
OTooley= totalcandidates.count("O'Tooley")

votos= len(totalvotos) 
kantPorcent= (Kant * 100)/votos   
CorreyPorcent= (Correy * 100)/votos
LiPorcent= (Li * 100)/votos  
OTooleyPorcent= (OTooley * 100)/votos

print("Elections Results")
print("-----------------------")
print(f"Total Votes: {votos}")
print(f"Kant: {kantPorcent}%  ({Kant})")
print(f"Correy: {CorreyPorcent}% ({Correy})")
print(f"Li: {LiPorcent}% ({Li})")
print(f"O'Tooley: {OTooleyPorcent}% ({OTooley})")
print("-----------------------")
print('Winner: Kant')
print("-----------------------")

with open("analysis.txt", "a") as f:
    print("Elections Results", file=f)
    print("-----------------------", file=f)
    print(f"Total Votes: {votos}", file=f)
    print(f"Kant: {kantPorcent}%  ({Kant})", file=f)
    print(f"Correy: {CorreyPorcent}% ({Correy})", file=f)
    print(f"Li: {LiPorcent}% ({Li})", file=f)
    print(f"O'Tooley: {OTooleyPorcent}% ({OTooley})", file=f)
    print("-----------------------", file=f)
    print('Winner: Kant', file=f)
    print("-----------------------", file=f)
    