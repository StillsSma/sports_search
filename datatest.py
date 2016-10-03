import csv

with open('sports.csv', 'rt') as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        for index, x in enumerate(row):
            if x == '':
                row[index] = 0

        data.append(row)

del data[0:3]

for row in data:
    del row[6:14]
    del row[0]

print (data)
