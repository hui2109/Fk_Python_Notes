import csv

filename = 'guangzhou-2017.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    first_row = next(reader)
    print(first_row)
