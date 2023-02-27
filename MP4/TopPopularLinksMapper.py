#!/usr/bin/env python3

import sys

word_dict = {}

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    if word not in word_dict.keys():
        word_dict[word] = count
    else:
        word_dict[word] += count 

sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_word_dict[:10]:
    print(f'{word}\t{count}')