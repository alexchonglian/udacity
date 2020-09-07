import pandas as pd
df = pd.read_csv('player_data.csv')
df.to_json('player_data2.json', orient='records', indent=4)