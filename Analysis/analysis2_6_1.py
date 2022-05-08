import pandas as pd 
import ast
import re

corpus = []

df = pd.read_csv("./Dataset/clean_4.csv")

for i in range(len(df)):
    x = df.iloc[i]['Tokenized']
    val = ast.literal_eval(x)
    store = []
    for v in val:
        if(not re.search("^[0-9].*", v)):
            store.append(v)

    corpus.append(store)



df['Tokenized'] = corpus
df.to_csv("./Dataset/clean2_4.csv", index = False)


