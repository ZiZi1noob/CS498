#!/usr/bin/env python3

import sys
import string

stopwords_path = sys.argv[1]
delimi_path = sys.argv[2]

with open(stopwords_path) as f:
    lines = f.readlines()
    stopwords_arr = [line.strip() for line in lines]

with open(delimi_path) as f:
    deli_arr = f.readline()

for line in sys.stdin:
    line = line.strip()
    line = ''.join([char.lower() if char not in deli_arr else ' ' for char in line])
    words = [word for word in line.split() if word not in stopwords_arr]
    words_no_stop = [word for word in words if word not in stopwords_arr]
    for word in words_no_stop:
        print('%s\t%s'%(word,1))
        #print(f'{word}\t1')
