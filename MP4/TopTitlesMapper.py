#!/usr/bin/env python3
import sys

word_dict = {}

for line in sys.stdin:
    if len(line.strip().split('\t')) != 2:
        continue
    word, count = line.strip().split('\t')
    count = int(count)
    word_dict[word] = word_dict.get(word, 0) + count

word_dict_items = word_dict.items()
sorted_word_dict = sorted(word_dict_items, key=lambda x: x[1], reverse=True)

for word, count in sorted_word_dict[:10]:
    print(f'{word}\t{count}')
