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
ouput  = os.path.join("Analysis", "analysis.txt")
print(ouput)

with open(ouput, "w") as f:
    f.write("Elections Results\n")
    f.write("-----------------------\n")
    f.write(f"Total Votes: {votos}\n")
    f.write(f"Kant: {kantPorcent}%  ({Kant})\n")
    f.write(f"Correy: {CorreyPorcent}% ({Correy})\n")
    f.write(f"Li: {LiPorcent}% ({Li})\n")
    f.write(f"O'Tooley: {OTooleyPorcent}% ({OTooley})\n")
    f.write("-----------------------\n")
    f.write('Winner: Kant\n')
    f.write("-----------------------\n")
 