import pandas as pd
import pdb
import csv
import os

with open('output.txt', 'w') as f:
    pypoll_csv = os.path.join('.', 'resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
    
    print(f"\n Election Results \n")
    print(f"\n Election Results \n",file=f)
    print(f'-'*20)
    print(f'-'*20,file=f)

    #The total number of votes cast
    count_votes = 0
    with open(pypoll_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        next(csv_reader)# Skips the header row
        for row in csv_reader:
            count_votes = count_votes + 1
    print(f'Total Votes: {count_votes}')
    print(f'Total Votes: {count_votes}',file=f)
    print(f'-'*20)
    print(f'-'*20,file=f)

    #A complete list of candidates who received votes
    list_candidates = []
    dict_candidates = {}
    with open(pypoll_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        next(csv_reader)# Skips the header row
        for row in csv_reader:
            name = row[2]
            if list_candidates.count(name) < 1:#Check if candidate already exists in list
                list_candidates.append(name)
                dict_candidates[name] = 0
            dict_candidates[name] = dict_candidates[name] +1

    #The percentage of votes each candidate won

    #The total number of votes each candidate won
    for candidate in list_candidates:
        message = f'{candidate}: {dict_candidates[candidate]/count_votes*100:.3f}% ({dict_candidates[candidate]:.0f})'
        print(message)
        print(message, file=f)

    #The winner of the election based on popular vote.]

    #print(f'Winner: {winner}')
    def keywithmaxval(dict):#Returns max in a dict
        list_values = list(dict.values()) #List of values of each key
        list_keys = list(dict.keys()) #List of each key
        return list_keys[list_values.index(max(list_values))]

    print(f'-'*20)
    print(f'-'*20,file=f)
    winner = keywithmaxval(dict_candidates)
    print(f'Winner: {winner}')
    print(f'Winner: {winner}',file=f)
    print(f'-'*20)
    print(f'-'*20,file=f)

f.close()