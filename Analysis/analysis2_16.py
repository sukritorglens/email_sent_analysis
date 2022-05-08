import pandas as pd 
import networkx as nx 
from tqdm import tqdm 


G = nx.Graph()

df = pd.read_csv("./Dataset/data_with_topics_cleaned.csv")

graph = {}

for i in range(len(df)):
    source = df.iloc[i]['From']
    target = df.iloc[i]['To']
    weight = df.iloc[i]['Polarity']
    if source not in graph:
        graph[source] = {target: weight}

    else:
        if target not in graph[source]:
            graph[source][target] = weight
        else:
            graph[source][target] = (weight + graph[source][target])/2

for i in graph: 
    for j in graph[i]:
        G.add_edge(i,j,weight = graph[i][j])


degree_centrality = nx.degree_centrality(G)