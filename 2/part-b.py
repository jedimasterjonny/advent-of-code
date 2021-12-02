#!/usr/bin/env python3

h = 0
d = 0
x = 0

with open("in") as f:
    for line in f:
        split = line.split()
        if split[0] == "forward":
            h += int(split[1])
            d += x * int(split[1])
        elif split[0] == "down":
            x += int(split[1])
        elif split[0] == "up":
            x -= int(split[1])

print(h * d)
