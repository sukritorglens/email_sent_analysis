import pandas as pd 
import ast 
import json 
import datetime

filepath = "./Dataset/working2_2.csv"

print("[1] Reading csv at ", datetime.datetime.now())
df = pd.read_csv(filepath)

graph = {}
to_drop = []

print('[2] Making dictionary for graph at ', datetime.datetime.now())
for i in range(len(df)):
    li = []
    
    if type(df.iloc[i]['To']) == float:
        to_drop.append(i)
        continue

    li = df.iloc[i]['To'].split(',')
    if df.iloc[i]['From'] not in graph.keys():
        graph[df.iloc[i]['From']] = dict()
    for j in li: 
        if(j not in graph[df.iloc[i]['From']].keys()):
            graph[df.iloc[i]['From']][j] = df.iloc[i]['Polarity']
        else:
            graph[df.iloc[i]['From']][j] = (graph[df.iloc[i]['From']][j] + df.iloc[i]['Polarity'])/2


print("[3] Creating json object at ", datetime.datetime.now())
js = json.dumps(graph, indent = 4)
print("[4] Writing to json file at ", datetime.datetime.now())
with open("./json/graph.json", "w") as outfile:
    outfile.write(js)
print('done!!!')

