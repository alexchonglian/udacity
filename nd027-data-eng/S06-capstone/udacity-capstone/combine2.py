import csv, json
from collections import Counter

in_path1 = 'player_data.csv'
json_path = 'player_data.json'

# combine
with open(in_path1) as csvFile:
    csvReader = csv.DictReader(csvFile)
    in_data1 = {i:dict(row) for i, row in enumerate(csvReader)}

with open(json_path, 'w') as jsonFile:
    jsonFile.write(json.dumps(in_data1, indent=4))