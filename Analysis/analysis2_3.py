import pandas as pd 

df1 = pd.read_csv("./Dataset/data2_7.csv")
df2 = pd.read_csv("./Dataset/data2_8.csv")
df3 = pd.read_csv("./Dataset/data2_9.csv")
df4 = pd.read_csv("./Dataset/data2_10.csv")

df1 = df1.append(df2)
df1 = df1.append(df3)
df = df1.append(df4)

df.to_csv("./Dataset/working2_1.csv", index = False)

print(len(df))