#!/usr/bin/env python3
import sys  


link_dict = {}
for line in sys.stdin:
    id_, val_ = line.strip().split('\t')
    if int(val_) == 0:
        if id_ not in link_dict.keys():
            link_dict[id_] = val_
    else:
        link_dict[id_] = val_


res_arr = []
for key, val in link_dict.items():
    key = int(key)
    val = int(val)
    if val == 0:
        res_arr.append(int(key))

for i in sorted(res_arr):
    print(i)