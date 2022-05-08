# NPS Calculation

import pandas as pd 
from tqdm import tqdm 

filepath = "./Dataset/enron_topic.csv"



df = pd.read_csv(filepath)

detractor = 0
promoter = 0


for i in tqdm(range(len(df))):
    if(df.iloc[i]['Polarity'] > 0):
        promoter += 1
    if(df.iloc[i]['Polarity'] < 0):
        detractor += 1


print("promoter %: ", (promoter)/len(df)*100)
print("detractor %: ", (detractor)/len(df)*100)
print("NPS Score : ", ((promoter)/len(df)-(detractor)/len(df))*100)