import csv, json
from collections import Counter

in_path1 = 'player_data.csv'
in_path2 = 'Players.csv'

# check duplicate names
with open(in_path1) as csvFile:
    csvReader = csv.reader(csvFile)
    names = [row[0] for row in csvReader]
names_set = set()
print(in_path1, names[:10])
for name in names:
    if name in names_set:
        print('duplicate name', name)
    names_set.add(name)


# check duplicate names
with open(in_path2) as csvFile:
    csvReader = csv.reader(csvFile)
    names = [row[1] for row in csvReader]
print(in_path2, names[:10])
names_set = set()
for name in names:
    if name in names_set:
        print('duplicate name', name)
    names_set.add(name)

# combine
with open(in_path1) as csvFile:
    csvReader = csv.DictReader(csvFile)
    in_data1 = [dict(row) for row in csvReader]

print(in_data1[:10])