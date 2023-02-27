#!/usr/bin/env python3

import sys
temp_dic = {}
for line in sys.stdin:
    word, count = line.strip().split('\t')
    temp_dic.update({word: int(count)})

sorted_dic = sorted(temp_dic.items(), key=lambda x: x[1], reverse=False)
for word, count in sorted_dic:
    print("%s\t%s"%(word,count))