from __future__ import print_function
import datetime
import json
import re
import pandas as pd 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import threading


filepath = "./Dataset/data4.csv"
tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words()

df = pd.read_csv(filepath)

li = []

# tokenizing the emails
def tokenize_emails(df, li):
    for i in range(len(df)):
        message = tokenizer.tokenize(df.iloc[i]['Content'])
        li.append(message)

# removing all stopwords in the corpus
def rem_stopwords(li): 
    for i in range(len(li)):
        temp = []
        for x in range(len(li[i])): 
            if(li[i][x] not in stop_words):
                temp.append(li[i][x])
        li[i] = temp

# lemmatization
def lemmatize_emails(li):
    for i in range(len(li)):
        for x in range(len(li[i])):
            li[i][x] = lemmatizer.lemmatize(li[i][x])
            if(len(li[i][x]) > 12): 
                li[i].remove(li[i][x])
            if(re.search("\*.*",li[i][x])):
                li[i].remove(li[i][x])


if __name__ == "__main__":
    # creating thread
    print('[1] Reading the csv file', datetime.datetime.now())
    df = pd.read_csv(filepath)
    df.drop(['Unnamed: 0'], axis = 1, inplace = True)
    print(df.columns)


    li1 = []
    li2 = []
    li3 = []
    li4 = []
    li5 = []
    li6 = []
    li7 = []
    li8 = []

    partition = int(len(df)/8)

    print('[2] Initializing multi-thread 1 at ', datetime.datetime.now())
    t1 = threading.Thread(target=tokenize_emails, args=(df[:partition], li1,))
    t2 = threading.Thread(target=tokenize_emails, args=(df[partition:2*partition], li2,))
    t3 = threading.Thread(target=tokenize_emails, args=(df[2*partition:3*partition], li3,))
    t4 = threading.Thread(target=tokenize_emails, args=(df[3*partition:4*partition], li4,))
    t5 = threading.Thread(target=tokenize_emails, args=(df[4*partition:5*partition], li5,))
    t6 = threading.Thread(target=tokenize_emails, args=(df[5*partition:6*partition], li6,))
    t7 = threading.Thread(target=tokenize_emails, args=(df[6*partition:7*partition], li7,))
    t8 = threading.Thread(target=tokenize_emails, args=(df[7*partition:], li8,))



    print('[3] Starting threads at ', datetime.datetime.now())
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
    # starting thread 4
    t4.start()
    # starting thread 5
    t5.start()
    # starting thread 6
    t6.start()
    # starting thread 7
    t7.start()
    # starting thread 8
    t8.start()
  
    print('[4] Joining threads at ', datetime.datetime.now())
    # starting thread 1
    t1.join()
    # joining thread 2
    t2.join()
    # joining thread 3
    t3.join()
    # joining thread 4
    t4.join()
    # joining thread 5
    t5.join()
    # joining thread 6
    t6.join()
    # joining thread 7
    t7.join()
    # joining thread 8
    t8.join()

    print('[5] Initializing multi-thread 2 at ', datetime.datetime.now())
    t1 = threading.Thread(target=rem_stopwords, args=(li[:partition],))
    t2 = threading.Thread(target=rem_stopwords, args=(li[partition:2*partition],))
    t3 = threading.Thread(target=rem_stopwords, args=(li[2*partition:3*partition],))
    t4 = threading.Thread(target=rem_stopwords, args=(li[3*partition:4*partition],))
    t5 = threading.Thread(target=rem_stopwords, args=(li[4*partition:5*partition],))
    t6 = threading.Thread(target=rem_stopwords, args=(li[5*partition:6*partition],))
    t7 = threading.Thread(target=rem_stopwords, args=(li[6*partition:7*partition],))
    t8 = threading.Thread(target=rem_stopwords, args=(li[7*partition:],))



    print('[6] Starting threads at ', datetime.datetime.now())
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
    # starting thread 4
    t4.start()
    # starting thread 5
    t5.start()
    # starting thread 6
    t6.start()
    # starting thread 7
    t7.start()
    # starting thread 8
    t8.start()
  
    print('[7] Joining threads at ', datetime.datetime.now())
    # joining thread 1
    t1.join()
    # joining thread 2
    t2.join()
    # joining thread 3
    t3.join()
    # joining thread 4
    t4.join()
    # joining thread 5
    t5.join()
    # joining thread 6
    t6.join()
    # joining thread 7
    t7.join()
    # joining thread 8
    t8.join()


    print('[8] Initializing multi-thread 3 at ', datetime.datetime.now())
    t1 = threading.Thread(target=lemmatize_emails, args=(li[:partition],))
    t2 = threading.Thread(target=lemmatize_emails, args=(li[partition:2*partition],))
    t3 = threading.Thread(target=lemmatize_emails, args=(li[2*partition:3*partition],))
    t4 = threading.Thread(target=lemmatize_emails, args=(li[3*partition:4*partition],))
    t5 = threading.Thread(target=lemmatize_emails, args=(li[4*partition:5*partition],))
    t6 = threading.Thread(target=lemmatize_emails, args=(li[5*partition:6*partition],))
    t7 = threading.Thread(target=lemmatize_emails, args=(li[6*partition:7*partition],))
    t8 = threading.Thread(target=lemmatize_emails, args=(li[7*partition:],))
    


    print('[9] Starting threads at ', datetime.datetime.now())
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
    # starting thread 4
    t4.start()
    # starting thread 5
    t5.start()
    # starting thread 6
    t6.start()
    # starting thread 7
    t7.start()
    # starting thread 8
    t8.start()
  
    print('[10] Joining threads at ', datetime.datetime.now())
    # starting thread 1
    t1.join()
    # joining thread 2
    t2.join()
    # joining thread 3
    t3.join()
    # joining thread 4
    t4.join()
    # joining thread 5
    t5.join()
    # joining thread 6
    t6.join()
    # joining thread 7
    t7.join()
    # joining thread 8
    t8.join()


    print('[11] Creating tokenized corpus at ', datetime.datetime.now())
    li = li1 + li2 + li3 + li4 + li5 + li6 + li7 + li8


    print('[12] Removing all whitespaces in the corpus at ', datetime.datetime.now())
    # removing any whitespace in the words in the list 
    for i in range(len(li)): 
        for x in range(len(li[i])): 
            li[i][x] = li[i][x].strip()
    
    print('[13] Storing the length of individual emails in the corpus at ', datetime.datetime.now())
    len_li = []
    for i in li:
        len_li.append(len(i))


    df['Tokenized'] = li
    
    # df.sort_values('Email_Size',inplace = True, ascending = False)
    print('[14] Storing the json in a file')

    dic = {"len_li": len_li}
    js = json.dumps(dic)
    
    with open("length.json", "w") as outfile:
        outfile.write(js)
    
    print('[15] Stored the json file')
    df.drop(['Content'], axis = 1, inplace = True)
    print('[16] Dropped the content column and storing the database')
    df.to_csv('./Dataset/data2_1.csv', index = False)
    print('[17] Done!!')