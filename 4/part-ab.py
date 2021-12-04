#!/usr/bin/env python3


def win(b):
    return any(all(i == -1 for i in line) for line in b) or any(
        all(line[idx] == -1 for line in b) for idx in range(len(b[0]))
    )


def score(idx, turn):
    return sum(sum(i for i in line if i != -1) for line in boards[idx]) * turn


lines = open("in").read().split("\n\n")
inp = [int(i) for i in lines[0].split(",")]
boards = [[[int(i) for i in line.split()] for line in b.split("\n")] for b in lines[1:]]

a_complete = False
for turn in inp:
    boards = [b for b in boards if not win(b)]
    boards = [[[-1 if i == turn else i for i in line] for line in b] for b in boards]

    # skip win checking if we've completed part a
    if a_complete and len(boards) > 1:
        continue

    winner = [win(b) for b in boards]
    if True in winner:
        if not a_complete:
            print("part a:", score(winner.index(True), turn))
            a_complete = True
        else:
            print("part b:", score(winner.index(True), turn))
            break
