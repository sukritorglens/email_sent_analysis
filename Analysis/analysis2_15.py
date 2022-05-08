## Plotting the number of emails topic wise 
import pandas as pd 
import matplotlib.pyplot as plt
from tqdm import tqdm 
import ast 

filepath = "./Dataset/data_with_topics_cleaned.csv"

df = pd.read_csv(filepath)

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])


dic = {"STATISTICS/ANALYTICS": 0,"FINANCE/BUSINESS": 0,"HEALTH/BIOLOGY": 0,"CLOTHING/FASHION": 0,
     "SPORTS": 0, "MILITARY_ACTION/POLITICS": 0, "CUISINE": 0}

li = ["STATISTICS/ANALYTICS","FINANCE/BUSINESS","HEALTH/BIOLOGY","CLOTHING/FASHION",
     "SPORTS", "MILITARY_ACTION/POLITICS", "CUISINE"]


li2 = []

for i in tqdm(range(len(df)), desc = "... Starting the count ..."):
    x = ast.literal_eval(df.iloc[i]['Topics'])
    for j in x: 
        dic[j] += 1

for i in dic: 
    li2.append(dic[i])

fig, ax = plt.subplots()
plt.figure(figsize=(20, 10))  # width:20, height:3
plt.bar(li, li2, align='edge', width=0.3)
addlabels(li, li2)
plt.xlabel("TOPICS")
plt.ylabel("NUMBER OF EMAILS")
plt.show()