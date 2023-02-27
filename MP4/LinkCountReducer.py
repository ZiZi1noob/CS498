#!/usr/bin/env python3

import sys

link_dict = {}
for line in sys.stdin:
    child_link, _ = line.strip().split('\t')
    if child_link not in link_dict.keys():
        link_dict[child_link] = 1
    else:
        link_dict[child_link] += 1

    
    
for link, count in link_dict.items():
    print(f'{link}\t{count}')
