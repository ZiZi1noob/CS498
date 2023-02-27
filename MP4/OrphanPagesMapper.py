#!/usr/bin/env python3

import sys


# data_path = r'./dataset/links/links-b'
# with open(data_path) as f:
#     links = f.readlines()
#     for link in links:

for line in sys.stdin:
    parent_id, child_links_str = line.strip().split(':')
    child_links = child_links_str.split()
    if child_links:
        print(f'{parent_id}\t0')
        for c_link in child_links:
            if parent_id != c_link:
                print(f'{c_link}\t1')
