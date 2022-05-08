## store the polarity scores in a json 

import pandas as pd 
import json 

df = pd.read_csv("./Dataset/working2_1.csv")

li = list(df['Polarity'])

dic = {'pol_scores': li}

js = json.dumps(dic)

with open("./json/pol_scores.json", "w") as outfile:
    outfile.write(js)