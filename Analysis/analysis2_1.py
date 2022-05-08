import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import ast 
import pandas as pd 
import threading 
import datetime 

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def get_polarity_score(df, pol_li, subj_li):
    for i in range(len(df)):
        x = ast.literal_eval(df.iloc[i]['Tokenized'])
        text = " ".join(x)
        doc = nlp(text)
        subj_li.append(doc._.blob.subjectivity)
        pol_li.append(doc._.doc._.blob.polarity)


if __name__ == "__main__":  

    print("[1] Reading the csv file at", datetime.datetime.now())
    ## Reading the csv file     
    filepath = "./Dataset/data2_6.csv"
    df = pd.read_csv(filepath)
    df = df[:int(len(df)/2)]

    pol_li1 = []
    pol_li2 = []
    pol_li3 = []
    pol_li4 = []
    pol_li5 = []
    pol_li6 = []
    pol_li7 = []
    pol_li8 = []
    pol_li9 = []
    pol_li10 = []
    pol_li11 = []
    pol_li12 = []
    pol_li13 = []
    pol_li14 = []
    pol_li15 = []

    subj_li1 = []
    subj_li2 = []
    subj_li3 = []
    subj_li4 = []
    subj_li5 = []
    subj_li6 = []
    subj_li7 = []
    subj_li8 = []
    subj_li9 = []
    subj_li10 = []
    subj_li11 = []
    subj_li12 = []
    subj_li13 = []
    subj_li14 = []
    subj_li15 = []


    partition = int(len(df)/15)

    print("[3] Initialising the threads at ", datetime.datetime.now()) 
    t1 = threading.Thread(target=get_polarity_score, args=(df[:partition],pol_li1, subj_li1))
    t2 = threading.Thread(target=get_polarity_score, args=(df[partition:2*partition],pol_li2, subj_li2))
    t3 = threading.Thread(target=get_polarity_score, args=(df[2*partition:3*partition],pol_li3, subj_li3))
    t4 = threading.Thread(target=get_polarity_score, args=(df[3*partition:4*partition],pol_li4, subj_li4))
    t5 = threading.Thread(target=get_polarity_score, args=(df[4*partition:5*partition],pol_li5, subj_li5))
    t6 = threading.Thread(target=get_polarity_score, args=(df[5*partition:6*partition],pol_li6, subj_li6))
    t7 = threading.Thread(target=get_polarity_score, args=(df[6*partition:7*partition],pol_li7, subj_li7))
    t8 = threading.Thread(target=get_polarity_score, args=(df[7*partition:8*partition],pol_li8, subj_li8))
    t9 = threading.Thread(target=get_polarity_score, args=(df[8*partition:9*partition], pol_li9, subj_li9))
    t10 = threading.Thread(target=get_polarity_score, args=(df[9*partition:10*partition],pol_li10, subj_li10))
    t11 = threading.Thread(target=get_polarity_score, args=(df[10*partition:11*partition],pol_li11, subj_li11))
    t12 = threading.Thread(target=get_polarity_score, args=(df[11*partition:12*partition],pol_li12, subj_li12))
    t13 = threading.Thread(target=get_polarity_score, args=(df[12*partition:13*partition],pol_li13, subj_li13))
    t14 = threading.Thread(target=get_polarity_score, args=(df[13*partition:14*partition],pol_li14, subj_li14))
    t15 = threading.Thread(target=get_polarity_score, args=(df[14*partition:],pol_li15, subj_li15))

    print("[4] Starting the threads at", datetime.datetime.now())
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

    print("[6] Threads have been joined lists are being concatanated at ", datetime.datetime.now())
    pol_li = pol_li1 + pol_li2 + pol_li3 + pol_li4 + pol_li5 + pol_li6 + pol_li7 + pol_li8 + pol_li9 + pol_li10 + pol_li11 + pol_li12 + pol_li13 + pol_li14 + pol_li15
    subj_li = subj_li1 + subj_li2 + subj_li3 + subj_li4 + subj_li5 + subj_li6 + subj_li7 + subj_li8 + subj_li9 + subj_li10 + subj_li11 + subj_li12 + subj_li13 + subj_li14 + subj_li15

    
    df['Polarity'] = pol_li
    df['Subjectivity'] = subj_li

    print("[7] Storing the file at ", datetime.datetime.now())
    df.to_csv("data2_7.csv", index = False)
    print("[8] Done!!! ")