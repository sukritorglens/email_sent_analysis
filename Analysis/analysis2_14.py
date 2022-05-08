import pandas as pd 
from tqdm import tqdm 
import ast 
import datetime 


filepath = "./Dataset/data_with_topics_cleaned.csv"

df = pd.read_csv(filepath)

print(list(df.columns))

def create_for_STATISTICS():
    temp_df = pd.DataFrame(columns = list(df.columns))
    for i in tqdm(range(len(df))):
        x = df.iloc[i]['Topics']
        x = ast.literal_eval(x)
        if('STATISTICS/ANALYTICS' in x):
            store = dict(df.iloc[i])
            temp_df = temp_df.append(store, ignore_index = True)

    temp_df.to_csv("./Dataset/topic_STATISTICS.csv")



def create_for_FINANCE():
    temp_df = pd.DataFrame(columns = list(df.columns))
    for i in tqdm(range(len(df))):
        x = df.iloc[i]['Topics']
        x = ast.literal_eval(x)
        if('FINANCE/BUSINESS' in x):
            store = dict(df.iloc[i])
            temp_df = temp_df.append(store, ignore_index = True)

    temp_df.to_csv("./Dataset/topic_FINANCE.csv")


def create_for_BIOLOGY():
    temp_df = pd.DataFrame(columns = list(df.columns))
    for i in tqdm(range(len(df))):
        x = df.iloc[i]['Topics']
        x = ast.literal_eval(x)
        if('HEALTH/BIOLOGY' in x):
            store = dict(df.iloc[i])
            temp_df = temp_df.append(store, ignore_index = True)

    temp_df.to_csv("./Dataset/topic_BIOLOGY.csv")


def create_for_CLOTHING():
    temp_df = pd.DataFrame(columns = list(df.columns))
    for i in tqdm(range(len(df))):
        x = df.iloc[i]['Topics']
        x = ast.literal_eval(x)
        if('CLOTHING/FASHION' in x):
            store = dict(df.iloc[i])
            temp_df = temp_df.append(store, ignore_index = True)

    temp_df.to_csv("./Dataset/topic_CLOTHING.csv")


def create_for_SPORTS():
    temp_df = pd.DataFrame(columns = list(df.columns))
    for i in tqdm(range(len(df))):
        x = df.iloc[i]['Topics']
        x = ast.literal_eval(x)
        if('SPORTS' in x):
            store = dict(df.iloc[i])
            temp_df = temp_df.append(store, ignore_index = True)

    temp_df.to_csv("./Dataset/topic_SPORTS.csv")

def create_for_MILITARY_ACTION():
    temp_df = pd.DataFrame(columns = list(df.columns))
    for i in tqdm(range(len(df))):
        x = df.iloc[i]['Topics']
        x = ast.literal_eval(x)
        if('MILITARY_ACTION/POLITICS' in x):
            store = dict(df.iloc[i])
            temp_df = temp_df.append(store, ignore_index = True)

    temp_df.to_csv("./Dataset/topic_MILITARY_ACTION.csv")




def create_for_CUISINE():
    temp_df = pd.DataFrame(columns = list(df.columns))
    for i in tqdm(range(len(df))):
        x = df.iloc[i]['Topics']
        x = ast.literal_eval(x)
        if('CUISINE' in x):
            store = dict(df.iloc[i])
            temp_df = temp_df.append(store, ignore_index = True)

    temp_df.to_csv("./Dataset/topic_CUISINE.csv")



print("[1] Creating for stats... ", datetime.datetime.now())
create_for_STATISTICS()
print("[2] Creating for sports ... ", datetime.datetime.now())
create_for_SPORTS()
print("[3] Creating for military_action ... ", datetime.datetime.now())
create_for_MILITARY_ACTION()
print("[4] Creating for finance ... ", datetime.datetime.now())
create_for_FINANCE()
print("[5] Creating for cuisine ... ", datetime.datetime.now())
create_for_CUISINE()
print("[6] Creating for clothing ... ", datetime.datetime.now())
create_for_CLOTHING()
print("[7] Creating for biology ... ", datetime.datetime.now())
create_for_BIOLOGY()
print("done !!!")