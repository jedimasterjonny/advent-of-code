#!/usr/bin/env python3

count = 0

with open("in") as f:
    prev = int(next(f))
    for line in f:
        if int(line) > prev:
            count += 1
        prev = int(line)

print(count)
