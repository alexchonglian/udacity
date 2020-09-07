import pandas as pd
#Examples

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])

print(df.to_json(orient='split'), end='\n\n')
#'{"columns":["col 1","col 2"],
#  "index":["row 1","row 2"],
#  "data":[["a","b"],["c","d"]]}'
#Encoding/decoding a Dataframe using 'records' formatted JSON. Note that index labels are not preserved with this encoding.

print(df.to_json(orient='records'), end='\n\n')
#'[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]'
#Encoding/decoding a Dataframe using 'index' formatted JSON:

print(df.to_json(orient='index'), end='\n\n')
#'{"row 1":{"col 1":"a","col 2":"b"},"row 2":{"col 1":"c","col 2":"d"}}'
#Encoding/decoding a Dataframe using 'columns' formatted JSON:

print(df.to_json(orient='columns'), end='\n\n')
#'{"col 1":{"row 1":"a","row 2":"c"},"col 2":{"row 1":"b","row 2":"d"}}'
#Encoding/decoding a Dataframe using 'values' formatted JSON:

print(df.to_json(orient='values'), end='\n\n')
#'[["a","b"],["c","d"]]'
#Encoding with Table Schema

print(df.to_json(orient='table'), end='\n\n')
#'{"schema": {"fields": [{"name": "index", "type": "string"},
#                        {"name": "col 1", "type": "string"},
#                        {"name": "col 2", "type": "string"}],
#             "primaryKey": "index",
#             "pandas_version": "0.20.0"},
#  "data": [{"index": "row 1", "col 1": "a", "col 2": "b"},
#           {"index": "row 2", "col 1": "c", "col 2": "d"}]}'