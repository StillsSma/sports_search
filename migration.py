import psycopg2

import csv

import csv

with open('sports.csv', 'r') as f:
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


connection = psycopg2.connect("dbname=we_like_sports user=we_like_sports")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS corn_huskers;")

create_table_command = """
CREATE TABLE corn_huskers (
    Player varchar(50),
    Att int,
    Yds int,
    Avg REAL,
    TD  int
);
"""

cursor.execute(create_table_command)
for row in data:
    cursor.execute("INSERT INTO corn_huskers VALUES (%s, %s, %s, %s, %s)",
    (row[0], row[1], row[2], row[3], row[4]))

connection.commit()
cursor.close()
connection.close()
