import pandas as pd 

filepath = "./Dataset/working2_2.csv"

df = pd.read_csv(filepath)

df = df.sample(frac = 1).reset_index(drop=True)

df1 = df[:int(len(df)/4)]
df2 = df[int(len(df)/4):2*int(len(df)/4)]
df3 = df[2*int(len(df)/4):3*int(len(df)/4)]
df4 = df[3*int(len(df)/4):]



df1.to_csv("./Dataset/clean_1.csv", index = False)
df2.to_csv("./Dataset/clean_2.csv", index = False)
df3.to_csv("./Dataset/clean_3.csv", index = False)
df4.to_csv("./Dataset/clean_4.csv", index = False)