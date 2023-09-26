import csv
with open('../src/items.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

s = '5.5'
print(int(float(s)))