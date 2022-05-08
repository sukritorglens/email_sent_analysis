import json
import ast 
import pandas as pd 
import threading


filepath1 = "./Dataset/data2_4.csv"
filepath2 = "./Dataset/data2_5.csv"

df1 = pd.read_csv(filepath1)
df2 = pd.read_csv(filepath2)

df1.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)
df2.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)

df = df1 + df2 

df.to_csv("./Dataset/data2_6.csv", index = False)
