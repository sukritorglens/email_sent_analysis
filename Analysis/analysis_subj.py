import pandas as pd 
from tqdm import tqdm 
import ast 
import datetime 
from textblob import TextBlob




def create_for_BIOLOGY():
    filepath = "./Dataset/topic_BIOLOGY.csv"
    df = pd.read_csv(filepath)
    li = []
    for i in tqdm(range(len(df)), desc = "...for BIOLOGY"):
        x = " ".join(ast.literal_eval(df.iloc[i]['Tokenized']))
        li.append(TextBlob(x).sentiment[1])
    df['Subjectivity'] = li
    df.to_csv(filepath)

def create_for_FINANCE():
    filepath = "./Dataset/topic_FINANCE.csv"
    df = pd.read_csv(filepath)
    li = []
    for i in tqdm(range(len(df)), desc = "...for FINANCE"):
        x = " ".join(ast.literal_eval(df.iloc[i]['Tokenized']))
        li.append(TextBlob(x).sentiment[1])
    df['Subjectivity'] = li
    df.to_csv(filepath)



def create_for_CLOTHING():
    filepath = "./Dataset/topic_CLOTHING.csv"
    df = pd.read_csv(filepath)
    li = []
    for i in tqdm(range(len(df)), desc = "...for CLOTHING"):
        x = " ".join(ast.literal_eval(df.iloc[i]['Tokenized']))
        li.append(TextBlob(x).sentiment[1])
    df['Subjectivity'] = li
    df.to_csv(filepath)


def create_for_CUISINE():
    filepath = "./Dataset/topic_CUISINE.csv"
    df = pd.read_csv(filepath)
    li = []
    for i in tqdm(range(len(df)), desc = "...for CUISINE"):
        x = " ".join(ast.literal_eval(df.iloc[i]['Tokenized']))
        li.append(TextBlob(x).sentiment[1])
    df['Subjectivity'] = li
    df.to_csv(filepath)


def create_for_MILITARY_ACTION():
    filepath = "./Dataset/topic_MILITARY_ACTION.csv"
    df = pd.read_csv(filepath)
    li = []
    for i in tqdm(range(len(df)), desc = "...for MILITARY_ACTION"):
        x = " ".join(ast.literal_eval(df.iloc[i]['Tokenized']))
        li.append(TextBlob(x).sentiment[1])
    df['Subjectivity'] = li
    df.to_csv(filepath)

def create_for_SPORTS():
    filepath = "./Dataset/topic_SPORTS.csv"
    df = pd.read_csv(filepath)
    li = []
    for i in tqdm(range(len(df)), desc = "...for SPORTS"):
        x = " ".join(ast.literal_eval(df.iloc[i]['Tokenized']))
        li.append(TextBlob(x).sentiment[1])
    df['Subjectivity'] = li
    df.to_csv(filepath)




def create_for_STATISTICS():
    filepath = "./Dataset/topic_STATISTICS.csv"
    df = pd.read_csv(filepath)
    li = []
    for i in tqdm(range(len(df)), desc = "...for STATISTICS"):
        x = " ".join(ast.literal_eval(df.iloc[i]['Tokenized']))
        li.append(TextBlob(x).sentiment[1])
    df['Subjectivity'] = li
    df.to_csv(filepath)



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