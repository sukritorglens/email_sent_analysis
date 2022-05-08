# DID NOT USE 

import pandas as pd 
import json 
import datetime
import torch 
import torchtext
from tqdm import tqdm 
import ast 

filepath = "./Dataset/clean2_3.csv"

print("[1] Reading the csv file ... ", datetime.datetime.now())
df = pd.read_csv(filepath)


print("[2] Reading the json file ... ", datetime.datetime.now())

f = open("./json/departments.json", 'r')
depts = json.load(f)

print("[3] Slicing the dataframe ... ", datetime.datetime.now())


print("[4] Storing the glove dataset ... ", datetime.datetime.now())
glove = torchtext.vocab.GloVe(name="6B",dim=100)

def dist_LEGAL_TEAM(doc):
    dist = 0
    for i in doc:
        for j in depts["LEGAL_TEAM"]:
            x = glove[i.lower()]
            y = glove[j.lower()]
            dist = dist + float(torch.norm(x-y))
    
    return dist


def dist_SALES(doc):
    dist = 0
    for i in doc:
        for j in depts["SALES"]:
            x = glove[i.lower()]
            y = glove[j.lower()]
            dist = dist + float(torch.norm(x-y))
    
    return dist


def dist_COMMUNICATION(doc):
    dist = 0
    for i in doc:
        for j in depts["COMMUNICATION"]:
            x = glove[i.lower()]
            y = glove[j.lower()]
            dist = dist + float(torch.norm(x-y))
    
    return dist

def dist_ENERGY_DESK(doc):
    dist = 0
    for i in doc:
        for j in depts["ENERGY_DESK"]:
            x = glove[i.lower()]
            y = glove[j.lower()]
            dist = dist + float(torch.norm(x-y))
    
    return dist

df = df[:int(len(df)/2)]

def find_department(doc):
    dist = {"LEGAL_TEAM": 0, "SALES": 0, "ENERGY_DESK": 0, "COMMUNICATION": 0}
    dist["LEGAL_TEAM"] = dist_LEGAL_TEAM(doc)
    dist["SALES"] = dist_SALES(doc)
    dist["ENERG_DESK"] = dist_ENERGY_DESK(doc)
    dist["COMMUNICATION"] = dist_COMMUNICATION(doc)
    
    return min(dist, key=dist.get)

print("[5] Calculating departments ... ", datetime.datetime.now())
li = []


for i in tqdm(range(len(df)), desc = "calculating..."):
    doc = df.iloc[i]['Tokenized']
    doc = ast.literal_eval(doc)
    dept = find_department(doc)

    li.append(dept)

print("[6] Storing the dataset ", datetime.datetime.now())
df['Department'] = li
df.to_csv("./Dataset/data_dept4.csv", index = False)
print(df["Department"].value_counts())
print("done!!!")
