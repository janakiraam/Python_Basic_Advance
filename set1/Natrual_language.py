# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:09:01 2018

@author: I340968
"""
import nltk
papers={'Madison':[10,14,37,38,39,40,41,42,43,44,45,46,47,48],
         'Hamilton':[1,6,7,8,9],
         'Jay':[2,3,4,5],
         'Shared':[18,19,20],
         'Disputed':[49,50,51,52,53,54]}

def read_files(filename):
    strings = []
    for file in filename:
        with open(f'data:\federalist_{file}.txt') as f:
            strings.append(f.read())
            
            
    return ('\n'.join(strings))

federalist_by_author ={}
for author,files in papers.items():
    federalist_by_author[author] = read_files(files)

#for author in papers:
#    print(federalist_by_author[author][:100])

authors = ('Hamilton','Madison','Disputed','Jay','Shared')

author_tokens = {}
length_distribution={}

for author in authors:
    tokens = nltk.word_tokenize(federalist_by_author[author])
    
    author_tokens[author] = ([token for token in tokens if any(c.isalpha() for c in token)])
    
    token_lengths = [len(token) for token in author_tokens[author]]
    length_distribution[authors]=nltk.FreqDist(token_lengths)
    length_distribution[authors].plot(15, title=author)