import pandas as pd 
import ast 
from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import DataFrame
import datetime

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel, TfidfModel


import pyLDAvis
import pyLDAvis.gensim_models


def make_bigrams(texts):
    print("In the bi-function ")
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts):
    print("In the tri-function")
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

corpus = []

filepath = "./Dataset/clean2_4.csv"

df = pd.read_csv(filepath)
df = df[20000:40000]

for i in range (len(df)):
    val = df.iloc[i]['Tokenized']
    val = ast.literal_eval(val)
    corpus.append(val)


data_words = corpus
for i in range(len(df)):
    temp = []
    val = df.iloc[i]['Tokenized']
    x = ast.literal_eval(val)
    corpus.append(x)

data_words = corpus

print("Creating bigram at ", datetime.datetime.now())
bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher threshold fewer phrases.
print("Creating trigram")
trigram = gensim.models.Phrases(bigram[df['Tokenized']], threshold=100)  

print("Creating bigram mod", datetime.datetime.now())
bigram_mod = gensim.models.phrases.Phraser(bigram)
print("Creating trigram mod")
trigram_mod = gensim.models.phrases.Phraser(trigram)


# Form Bigrams
print('Making the bigram at ', datetime.datetime.now())
data_words_bigrams = make_bigrams(data_words)
print("Making the trigram at ", datetime.datetime.now())
data_words_trigrams = make_trigrams(data_words_bigrams)

print("Starting tfidf")
id2word = corpora.Dictionary(data_words_trigrams)

texts = data_words_trigrams
corpus = [id2word.doc2bow(text) for text in texts]


tfidf = TfidfModel(corpus, id2word = id2word)

low_value = 0.3 
words = []
words_missing_in_tfidf = []


print("Step 2 of tfidf")
for i in range(0,len(corpus)):
    if(i == int(len(corpus)/4)):
        print("finished 25% at ", datetime.datetime.now())
    if(i == int(len(corpus)/2)):
        print('finished 50% at', datetime.datetime.now())
    if(i == int(3*len(corpus)/4)):
        print('finished 75% at', datetime.datetime.now())
    bow = corpus[i]
    low_value_words = []
    tfidf_ids = [id for id, value in tfidf[bow]]
    bow_ids = [id for id, value in bow]
    low_value_words = [id for id, value in tfidf[bow] if value < low_value]
    drops = low_value_words + words_missing_in_tfidf
    for item in drops: 
        words.append(id2word[item])
    words_missing_in_tfidf = [id for id in bow_ids if id not in tfidf_ids]

    new_bow = [b for b in bow if b[0] not in low_value_words and b[0] not in words_missing_in_tfidf]
    corpus[i] = new_bow


print("Starting lda at ", datetime.datetime.now())
lda_model = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word = id2word, 
                                            num_topics = 8, 
                                             update_every=1, chunksize = 100, passes = 10, alpha = "auto")

print("Creating lda file at", datetime.datetime.now())
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds="mmds", R=15)
pyLDAvis.save_html(vis, './Clusters/lda4_2.html')
print('done')