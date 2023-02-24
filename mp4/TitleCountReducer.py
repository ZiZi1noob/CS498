#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO

# input comes from STDIN
word_dic = {}
for line in sys.stdin:
    # TODO
    word, occu = line.strip().split(' ')
    if word in word_dic.keys():
        word_dic[word] += int(occu)
    else:
        word_dic[word] = int(occu)
print(word_dic)
for key in word_dic.keys():
    print('%s\t%s' % (key, word_dic[key])) #pass this output to reducer