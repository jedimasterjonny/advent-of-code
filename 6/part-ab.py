#!/usr/bin/env python3

data = [0] * 10
for f in [int(x) for x in open("in").read().split(",")]:
    data[f] += 1

for day in range(1, 257):
    data[9] = data[0]
    data[7] += data[0]
    data[0:9] = data[1:]

print(sum(data[0:9]))
