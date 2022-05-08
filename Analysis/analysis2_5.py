import pandas as pd 
import math

filepath = "./Dataset/working2_1.csv"

df = pd.read_csv(filepath)
print(len(df))
li = []
to_drop = []
for i in range(len(df)):
    if(math.isnan(df.iloc[i]['Polarity'])):
        to_drop.append(i)

    li.append(abs(df.iloc[i]['Polarity']))


df.drop(to_drop, inplace = True)
df['Magnitude'] = li
df.sort_values(['Magnitude'], inplace = True, ascending = False)
print(df.head())
df.to_csv("./Dataset/working2_2.csv", index = False)