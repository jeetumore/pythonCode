import csv
import os

# with open('output4', 'r') as file:
#     for line in file:
#         print(line.strip())
#
filename = 'output6.csv'
data = []
with open(filename, mode='r', newline='') as csvFile:
    csv_file = csv.DictReader(csvFile)

    for key in csv_file:
        data.append(key)

