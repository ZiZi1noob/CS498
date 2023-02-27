#!/usr/bin/env python3

from operator import itemgetter
import sys

#TODO
word_dict = {}
for line in sys.stdin:
    line.strip()
    word, count = line.split('\t', 1)
    word_dict[word] = word_dict.get(word, 0) + 1

for word in word_dict:
    #print(f'{word}\t{word_dict.get(word)}')
    print('%s\t%s'%(word,word_dict.get(word)))
    
