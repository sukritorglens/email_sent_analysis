from django.forms import DateInput
import networkx as nx 
import matplotlib.pyplot as plt
import json 
import datetime

print("[1] Reading and loading json data at ", datetime.datetime.now())
filepath = "./json/graph.json"
f = open(filepath, 'r')
data = json.load(f)

print("[2] Generating nodes")
G = nx.DiGraph()
nodes = 0

for i in data:
    nodes += 1
    G.add_node(i)

for i in data:
    for j in data[i]:
        G.add_edge(i, j, weight = data[i][j])
print("Number of nodes: ", nodes)
nx.draw(G)
labels = nx.get_edge_attributes(G,'weight')
plt.savefig("./Graphs/graph1.png")
print("Finished at ", datetime.datetime.now())
print("done!!!")
