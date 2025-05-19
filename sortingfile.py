import csv
import pandas as pd


# def sortcsv(inputfile, outputfile, sortcolum, delimiter):
#     with open(inputfile, 'r'  , newline='') as input, open(outputfile, 'w', newline='') as output:
#         reader = csv.reader(input, delimiter=delimiter)
#         header = next(reader)
#         sortdata = sorted(reader, key=lambda row: row[sortcolum])
#
#         writer = csv.writer(output, delimiter=delimiter)
#         writer.writerow(header)
#         writer.writerows(sortdata)
#
#
# def sort_data(inputfile, outputfile, sortcolum, delimiter):
#     with open(inputfile, 'r', newline='') as inputfile, open(outputfile, 'w', newline='') as outputfile:
#         reader = csv.reader(inputfile, delimiter=delimiter)
#         header = next(reader)
#         sort_colum = sorted(reader, key=lambda row: row[sortcolum])
#
#         writer = csv.writer(outputfile, delimiter=delimiter)
#         writer.writerow(header)
#         writer.writerows(sort_colum)

def sort_data(inputFile, outputFile, sortcolum, delimeter):
    with open(inputFile, 'r', newline='') as input, open(outputFile, 'w', newline='') as output:
        reader = csv.reader(input, delimiter=delimeter)
        print(reader)
        header = next(reader)
        sort_colum = sorted(reader, key=lambda row: row[sortcolum])

        writer = csv.writer(output, delimiter=delimeter)
        writer.writerow(header)
        writer.writerows(sort_colum)



if __name__ == '__main__':
    inputfile = 'input.csv'
    outputfile = 'output11.csv'
    sortcolum = 0
    delimiter = ','

    sort_data(inputfile, outputfile, sortcolum, delimiter)














