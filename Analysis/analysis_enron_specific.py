import pandas as pd 
import json 
import ast
from tqdm import tqdm 


filepath = "./Dataset/working2_2.csv"
jsfile = "./json/enron_cluster.json"

df = pd.read_csv(filepath)
df2 = pd.DataFrame(columns = list(df.columns))


f = open(jsfile,'r')
data = json.load(f)

to_append = []

for i in tqdm(range(len(df)), desc = "..processing"):
    x = ast.literal_eval(df.iloc[i]['Tokenized'])
    for j in x: 
        if j in data: 
            to_append.append(i)

for i in to_append:
    df2 = df2.append(df.iloc[i])

df2.to_csv('./Dataset/enron_topic.csv')