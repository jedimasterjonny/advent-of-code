#!/usr/bin/env python3

import statistics

inp = [int(x) for x in open("in").read().split(",")]

print(sum([abs(x - statistics.median(inp)) for x in inp]))


def step(x):
    return x * (x + 1) // 2


print(sum(step(abs(x - (sum(inp) // len(inp)))) for x in sorted(inp)))
