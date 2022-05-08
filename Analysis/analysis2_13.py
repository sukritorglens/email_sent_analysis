import pandas as pd 
import ast 

filepath = "./Dataset/data_with_topics.csv"

df = pd.read_csv(filepath)

score = 0

to_drop = []
for i in range(len(df)):
    x = ast.literal_eval(df.iloc[i]['Topics'])
    if(len(x) == 0):
        to_drop.append(i)

df.drop(to_drop, axis = 0, inplace = True)

df.to_csv("./Dataset/data_with_topics_cleaned.csv", index = False)
