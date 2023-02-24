#!/usr/bin/env python3

import sys
import string
import re


# stopWordsPath = sys.argv[1]
# delimitersPath = sys.argv[2]


# # TODO
stopWordsPath = './stopwords.txt'
delimitersPath = './delimiters.txt'
stopwords_arr = ['']
with open(stopWordsPath) as file:
    # TODO
    stopwords = file.readlines()
    for stopword in stopwords:
        stopword = stopword.strip()
        if stopword not in stopwords_arr:
            stopwords_arr.append(stopword)



#TODO 
delimiters_arr = ''
with open(delimitersPath) as file:
    # TODO
    delimiters_arr = file.readlines()[0]


# for line in sys.stdin:



title_a = r'C:\Users\ZiZi\OneDrive - University of Illinois - Urbana\UIUC\CS498 Cloud Computing Application\MP4\PythonTemplate\dataset\titles\titles-a'
word_count_dic = {}
with open(title_a, encoding = 'utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = re.sub(r'[\,\;\.\?\!\-\:\@\[\]\(\)\{\}\_\*\/]+', ' ', line)
        for word in line.split(' '):
            word = word.lower()
            if word in stopwords_arr:
                continue
            if word in word_count_dic.keys():
                word_count_dic[word] += 1
            else:
                word_count_dic[word] = 1

word_count_dic = sorted(word_count_dic.items(), key=lambda x:x[1], reverse=True)
for i, j in enumerate(word_count_dic):
    if i == 10:
        break
    print('%s\t%s' % (j[0], j[1])) #pass this output to reducer


