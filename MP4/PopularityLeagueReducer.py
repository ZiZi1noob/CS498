#!/usr/bin/env python3

import sys

league_dict = {}

for line in sys.stdin:
    league_id, count = line.strip().split('\t')
    count = int(count)
    league_id = int(league_id)
    if count > 0:
        league_dict[league_id] = count

sorted_league_dict = sorted(league_dict.items(), key=lambda x: x[0], reverse=True)

for league_id, link_count in sorted_league_dict:
    rank = 0
    for item in league_dict:
        if league_dict.get(item) < link_count:
            rank += 1
    print(f'{league_id}\t{rank}')