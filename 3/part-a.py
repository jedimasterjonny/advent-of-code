#!/usr/bin/env python3

lines = 0

with open("in") as f:
    sums = [0] * len(f.readline().rstrip())

with open("in") as f:
    for line in f:
        lines += 1
        col = 0
        for ch in line:
            if ch != "\n":
                sums[col] += int(ch)
            col += 1

common = int("".join(str(e) for e in [1 if s >= lines / 2 else 0 for s in sums]), 2)
uncommon = int("".join(str(e) for e in [1 if s < lines / 2 else 0 for s in sums]), 2)

print(common * uncommon)
