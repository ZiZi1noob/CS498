#!/usr/bin/env python3

import sys

league_path = sys.argv[1]
league_dict = {}



with open(league_path) as f:
    leagues = f.readlines()
    for league in leagues:
        league = league.strip()
        league_dict[league] = 0


for line in sys.stdin:
    id_, count = line.strip().split('\t')
    if id_ in league_dict.keys():
        league_dict[id_] = int(count)

for league, count in league_dict.items():
    print(f'{league}\t{count}')
