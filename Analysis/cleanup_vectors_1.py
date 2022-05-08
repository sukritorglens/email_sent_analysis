import pandas as pd
import ast 
import threading
import datetime 


def write_corpus(df, li):
    for i in range(len(df)):
        x = ast.literal_eval(df.iloc[i]['Tokenized'])
        message = ' '.join(x)
        li.append(message)




if __name__ == "__main__":
    print("[1] Reading the csv file at", datetime.datetime.now())
    df = pd.read_csv("./Dataset/working2_2.csv")

    print("[2] Dropping irrelevant columns at", datetime.datetime.now())
    df.drop(['Polarity','Magnitude'], axis = 1, inplace = True)

    corpus = []

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

    df = df[3*int(len(df)/4):]

    partition = int(len(df)/15)
    print("[3] Initializing threads at ", datetime.datetime.now())
    t1 = threading.Thread(target=write_corpus, args=(df[:partition],li1))
    t2 = threading.Thread(target=write_corpus, args=(df[partition:2*partition],li2))
    t3 = threading.Thread(target=write_corpus, args=(df[2*partition:3*partition],li3))
    t4 = threading.Thread(target=write_corpus, args=(df[3*partition:4*partition],li4))
    t5 = threading.Thread(target=write_corpus, args=(df[4*partition:5*partition],li5))
    t6 = threading.Thread(target=write_corpus, args=(df[5*partition:6*partition],li6))
    t7 = threading.Thread(target=write_corpus, args=(df[6*partition:7*partition],li7))
    t8 = threading.Thread(target=write_corpus, args=(df[7*partition:8*partition],li8))
    t9 = threading.Thread(target=write_corpus, args=(df[8*partition:9*partition], li9))
    t10 = threading.Thread(target=write_corpus, args=(df[9*partition:10*partition],li10))
    t11 = threading.Thread(target=write_corpus, args=(df[10*partition:11*partition],li11))
    t12 = threading.Thread(target=write_corpus, args=(df[11*partition:12*partition],li12))
    t13 = threading.Thread(target=write_corpus, args=(df[12*partition:13*partition],li13))
    t14 = threading.Thread(target=write_corpus, args=(df[13*partition:14*partition],li14))
    t15 = threading.Thread(target=write_corpus, args=(df[14*partition:],li15))


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

    print("[6] Threads have been joined at ", datetime.datetime.now())

    corpus = li1 + li2 + li3 + li4 + li5 + li6 + li7 + li8 + li9 + li10 + li11 + li12 + li13 + li14 + li15

    print("[7] Storing the corpus in the dataframe at ", datetime.datetime.now())

    df['Content'] = corpus
    df.drop(['Tokenized'], axis = 1, inplace = True)
    print("[8] Writing dataframe to csv file at ", datetime.datetime.now())
    df.to_csv("./Dataset/vectors_train_data_4.csv", index = False)
    print("done!!!")