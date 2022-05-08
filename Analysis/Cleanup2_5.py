import pandas as pd 

filepath1 = "./Dataset/data2_4.csv"
filepath2 = "./Dataset/data2_5.csv"

df1 = pd.read_csv(filepath1)
df2 = pd.read_csv(filepath2)

df = df1.append(df2)
print(len(df))

df.to_csv("./Dataset/data2_6.csv", index = False)