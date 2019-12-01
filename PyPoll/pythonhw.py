import csv

with open("election_data.csv") as in_file:
    csv_reader = csv.reader(in_file)
    data = list(csv_reader)
    print("Election Results:")
    row_count = len(data)
    print("Total votes: ", row_count)
    candidates = []
    for row in data:
       candidates.append(row[2])
    #print(candidates)
    count = candidates.count('Khan')
    percent = int(count / row_count * 100) 
    print("Khan:", count, + percent, "%") 
    count = candidates.count('Correy')
    percent = int(count / row_count * 100) 
    print("Correy:", count, + percent, "%")
    count = candidates.count('Li')
    percent = int(count / row_count * 100) 
    print("Li:", count, + percent, "%")
    count = candidates.count("O'Tooley")
    percent = int(count / row_count * 100) 
    print("O'Tooley:", count, + percent, "%")
    mode = max(str(count))
    print(mode)
  
    