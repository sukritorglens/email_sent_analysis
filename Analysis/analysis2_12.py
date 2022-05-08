import pandas as pd 
import json 
import ast 
import datetime
from tqdm import tqdm 


print("[1] Reading the csv data file at ... ", datetime.datetime.now())
filepath = "./Dataset/clean2_4.csv"
df = pd.read_csv(filepath)

print("[2] Reading the json file at ... ", datetime.datetime.now())
f = open("labeled_clusters.json", 'r')
dic = json.load(f)

def get_list_of_topics(s):
    store = []
    for i in s: 
        if(len(store) == 7):
            return store
        for j in dic.keys():
            if j in store:
                break
            else:
                if i in dic[j]:
                    store.append(j)
    
    return store

li = []
for i in tqdm(range(len(df)), desc = "Getting topics..."):
    x = ast.literal_eval(df.iloc[i]['Tokenized'])
    s = set(x)
    li.append(get_list_of_topics(s))

df['Topics'] = li
df.to_csv("./Dataset/data_with_topics.csv", index = False)