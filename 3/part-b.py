#!/usr/bin/env python3


def uncommon_at(elems):
    if elems.count("1") == elems.count("0"):
        return "0"
    return min(set(elems), key=elems.count)


def common_at(elems):
    if elems.count("1") == elems.count("0"):
        return "1"
    return max(set(elems), key=elems.count)


def go(lines):
    oxy = lines
    co2 = lines
    for i in range(0, len(lines[0])):
        co2 = list(filter(lambda s: s[i] == uncommon_at([s[i] for s in co2]), co2))
        oxy = list(filter(lambda s: s[i] == common_at([s[i] for s in oxy]), oxy))
    return (oxy, co2)


def to_dec(inp):
    return int("".join(inp), 2)


with open("in") as file:
    (oxy, co2) = go([line.rstrip() for line in file.readlines()])
    print(to_dec(oxy) * to_dec(co2))
