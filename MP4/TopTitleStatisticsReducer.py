#!/usr/bin/env python3

import sys
import math

count_arr = []

for line in sys.stdin:
    line = line.strip()
    count_arr.append(int(line))



sum_ = sum(count_arr)
num_len = len(count_arr)
MEAN = math.floor(sum_ / num_len)
VAR = math.floor(sum([(count-MEAN)**2 for count in count_arr]) / num_len)


print(f'Mean\t{MEAN}')
print(f'Sum\t{sum(count_arr)}')
print(f'Min\t{min(count_arr)}')
print(f'Max\t{max(count_arr)}')
print(f'Var\t{VAR}')
