import json
import numpy as np
import re
from collections import Counter
import pickle
import torch
import torchtext.vocab as vocab
glove = vocab.GloVe(name='840B', dim=300)
from wordfreq import word_frequency, top_n_list
import time
# print(real_word, get_word(real_word))

top_words = top_n_list('en', 200000)
def get_word(word):
    return glove.vectors[glove.stoi[word]].numpy()


def word2vec(pkl_file):
    _file = open(pkl_file, "rb")
    data = pickle.load(_file)
    zero_embed = np.zeros(300)
    for d in data:
        print (d)
        json_file = d.replace('json','pkl')
        tmp_file = open(json_file, "rb")
        json_words = pickle.load(tmp_file)
        t1 =time.time()
        embeddings =  []
        for real_word in json_words:
            # if real_word in top_words:
            try:
                embed = get_word(real_word)
                # print(real_word, embed.shape,time.time() - t1)
                embeddings.append(embed)
            except:
                embeddings.append(zero_embed)
                # continue
        # break
        
        embeddings = np.asarray(embeddings)
        print (embeddings.shape)
        np.save(d.replace('json','npy'), embeddings)

word2vec('./pickle/all_file.pkl')



