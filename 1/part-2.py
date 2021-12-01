#!/usr/bin/env python3

import queue

count = 0
q = queue.Queue()

with open("in") as f:
    q.put(int(next(f)))
    q.put(int(next(f)))
    q.put(int(next(f)))
    prev = sum(list(q.queue))
    for line in f:
        if sum(list(q.queue)) > prev:
            count += 1
        prev = sum(list(q.queue))
        q.get()
        q.put(int(line))

if sum(list(q.queue)) > prev:
    count += 1

print(count)
