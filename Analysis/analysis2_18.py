from tqdm import tqdm
import string
import numpy as np 
import pandas as pd
import string, re
import collections 
import json 
import datetime
from sklearn.cluster import KMeans


print("[1] Reading the dataset at ", datetime.datetime.now())
emails_df = pd.read_csv("./Dataset/partitioned_data.csv")
GLOVE_DATASET_PATH = './Glove_Vectors/glove.840B.300d.txt'


emails_sample_df = emails_df.copy()


print("[2] Performing additional cleanup at ", datetime.datetime.now())
# clean up subject line
emails_sample_df['Subject'] = emails_sample_df['Subject'].str.lower()
emails_sample_df['Subject'] = emails_sample_df['Subject'].str.replace(r'[^a-z]', ' ')  
emails_sample_df['Subject'] = emails_sample_df['Subject'].str.replace(r'\s+', ' ')  

# clean up content line
emails_sample_df['Content'] = emails_sample_df['Content'].str.lower()
emails_sample_df['Content'] = emails_sample_df['Content'].str.replace(r'[^a-z]', ' ')  
emails_sample_df['Content'] = emails_sample_df['Content'].str.replace(r'\s+', ' ')  

print("[3] Creating Sentence List at ", datetime.datetime.now())
# create sentence list 
to_drop = []
for i in range(len(emails_sample_df)):
  if(type(emails_sample_df.iloc[i]['Subject']) == float):
    to_drop.append(i)

emails_sample_df.drop(to_drop, axis = 0, inplace = True)

emails_text = (emails_sample_df["Subject"] + ". " + emails_sample_df["Content"]).tolist()




sentences = ' '.join(emails_text)
words = sentences.split()

print('Data size', len(words))
 
print("[4] Getting unique words and mapping to glove dataset at ", datetime.datetime.now())
# get unique words and map to glove set
print('Unique word count', len(set(words))) 
 

# drop rare words
vocabulary_size = 100000

def build_dataset(words):
  count = [['UNK', -1]]
  count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
  dictionary = dict()
  for word, _ in count:
    dictionary[word] = len(dictionary)
  data = list()
  unk_count = 0
  for word in tqdm(words):
    if word in dictionary:
      index = dictionary[word]
    else:
      index = 0  # dictionary['UNK']
      unk_count += 1
    data.append(index)
  count[0][1] = unk_count
  reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
  return data, count, dictionary, reverse_dictionary

data, count, dictionary, reverse_dictionary = build_dataset(words)

del words  
print('Most common words (+UNK)', count[:5])
print('Sample data', data[:10], [reverse_dictionary[i] for i in data[:10]])


embeddings_index = {}


print("Opening the glove dataset at ", datetime.datetime.now())
f = open(GLOVE_DATASET_PATH, encoding = "utf-8")
word_counter = 0
for line in tqdm(f):
  try:
    values = line.split()
    word = values[0]
    if word in dictionary:
      coefs = np.asarray(values[1:], dtype='float32')
      embeddings_index[word] = coefs
    word_counter += 1
  except:
    continue

f.close()

print('Found %s word vectors matching enron data set.' % len(embeddings_index))
print('Total words in GloVe data set: %s' % word_counter)

print("[5] Creating clusters at ", datetime.datetime.now())
enrond_dataframe = pd.DataFrame(embeddings_index)
enrond_dataframe = pd.DataFrame.transpose(enrond_dataframe)
 
# See what it learns and look at clusters to pull out major themes in the data
CLUSTER_SIZE = 50 
# cluster vector and investigate top groups
kmeans = KMeans(n_clusters=CLUSTER_SIZE)
cluster_make = kmeans.fit_predict(enrond_dataframe)

labels = kmeans.predict(enrond_dataframe)
cluster_frequency = collections.Counter(labels)
print(cluster_frequency)
cluster_frequency.most_common()

clusters = {}
n = 0
for item in labels:
    if item in clusters:
        clusters[item].append(list(enrond_dataframe.index)[n])
    else:
        clusters[item] = [list(enrond_dataframe.index)[n]]
    n +=1

for k,v in cluster_frequency.most_common(100):
  print('\n\n')
  print('Cluster:', k)
  print (' '.join(clusters[k]))


print("[6] Writing into json file at ",datetime.datetime.now())

f_write = open("cluster_file.txt",'w')
f_write.writelines(str(clusters))

centroids = kmeans.cluster_centers_
cen_x = [i[0] for i in centroids] 
cen_y = [i[1] for i in centroids]


print(cen_x)
print(cen_y)

print("done!!!")