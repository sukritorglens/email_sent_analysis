## Dropped all emails under the lower quartile 

import datetime
import json
import threading
import pandas as pd 
import numpy as np 
import ast 

filepath = "./Dataset/data2_3.csv"
jsfile = "./json/length.json"
stop_set = ['is','our','to','a','the','you','me','us','we','the','i','at','on','this','that', 'stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I',
 'that', 'had', 'on', 'for', 'were', 'was', 'of', 'if', "then", 'or', 'as','be','go','way','get','here','have','their','there', "by", "are"]

li = []

def count_stopwords(df,new_corp):
    for i in df['Tokenized']:
        email = ast.literal_eval(i) 
        keep = []
        for x in email:
            if x not in stop_set:
                if len(x) > 1:
                    keep.append(x)
        new_corp.append(keep)



if __name__ == "__main__":

    print("[1] Reading csv file into dataframe at", datetime.datetime.now())
    df = pd.read_csv(filepath)
    
    print("[2] Reading json file for length of emails at", datetime.datetime.now())
    f = open(jsfile)
    data = json.load(f)
    len_li = data["len_li"]

    li1 = []
    li2 = []
    li3 = []
    li4 = []
    li5 = []
    li6 = []
    li7 = []
    li8 = []
    li9 = []
    li10 = []
    li11 = []
    li12 = []
    li13 = []
    li14 = []
    li15 = []

    new_corp1 = []
    new_corp2 = []
    new_corp3 = []
    new_corp4 = []
    new_corp5 = []
    new_corp6 = []
    new_corp7 = []
    new_corp8 = []
    new_corp9 = []
    new_corp10 = []
    new_corp11 = []
    new_corp12 = []
    new_corp13 = []
    new_corp14 = []
    new_corp15 = []

    ##     df = df[int(len(df)/2):]  do this for first half and second half separately 
    df = df[int(len(df)/2):]
    partition = int(len(df)/15)
    print("[3] Initializing threads at ", datetime.datetime.now())
    t1 = threading.Thread(target=count_stopwords, args=(df[:partition],new_corp1))
    t2 = threading.Thread(target=count_stopwords, args=(df[partition:2*partition],new_corp2))
    t3 = threading.Thread(target=count_stopwords, args=(df[2*partition:3*partition],new_corp3))
    t4 = threading.Thread(target=count_stopwords, args=(df[3*partition:4*partition],new_corp4))
    t5 = threading.Thread(target=count_stopwords, args=(df[4*partition:5*partition],new_corp5))
    t6 = threading.Thread(target=count_stopwords, args=(df[5*partition:6*partition],new_corp6))
    t7 = threading.Thread(target=count_stopwords, args=(df[6*partition:7*partition],new_corp7))
    t8 = threading.Thread(target=count_stopwords, args=(df[7*partition:8*partition],new_corp8))
    t9 = threading.Thread(target=count_stopwords, args=(df[8*partition:9*partition], new_corp9))
    t10 = threading.Thread(target=count_stopwords, args=(df[9*partition:10*partition],new_corp10))
    t11 = threading.Thread(target=count_stopwords, args=(df[10*partition:11*partition],new_corp11))
    t12 = threading.Thread(target=count_stopwords, args=(df[11*partition:12*partition],new_corp12))
    t13 = threading.Thread(target=count_stopwords, args=(df[12*partition:13*partition],new_corp13))
    t14 = threading.Thread(target=count_stopwords, args=(df[13*partition:14*partition],new_corp14))
    t15 = threading.Thread(target=count_stopwords, args=(df[14*partition:],new_corp15))


    print("[4] Initializing threads at", datetime.datetime.now())
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
    # starting thread 9
    t9.start()
    # starting thread 10
    t10.start()
    # starting thread 11
    t11.start()
    # starting thread 12
    t12.start()
    # starting thread 13
    t13.start()
    # starting thread 14
    t14.start()
    # starting thread 15
    t15.start()


    print("[5] Waiting for threads to join at ", datetime.datetime.now())
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
    # joining thread 9
    t9.join()
    # joining thread 10
    t10.join()
    # joining thread 11
    t11.join()
    # joining thread 12
    t12.join()
    # joining thread 13
    t13.join()
    # joining thread 14
    t14.join()
    # joining thread 15
    t15.join()
    new_corp = []
    print("[6] Threads joined, now combining corpus list at ", datetime.datetime.now())
    new_corp = new_corp1 + new_corp2 + new_corp3 + new_corp4 + new_corp5 + new_corp6 + new_corp7 + new_corp8 + new_corp9 + new_corp10 + new_corp11 + new_corp12 + new_corp13 + new_corp14 + new_corp15
    print("[7] Assigning new_corp to Tokenized column at ", datetime.datetime.now())
    
    df['Tokenized'] = new_corp



    print("[8] Calculating to_drop list at", datetime.datetime.now())
    lower_lim = np.quantile(len_li, 0.25)


    print("[9] Saving to csv at ", datetime.datetime.now())
    df.to_csv("./Dataset/data2_5.csv")
    print("[10] Done!!! Length of df = ", len(df), " done at time ", datetime.datetime.now())