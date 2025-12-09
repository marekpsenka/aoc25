import fileinput
from math import sqrt
from itertools import combinations
from operator import itemgetter

input = map(str.rstrip, fileinput.input())

Point = tuple[int, int, int]


def dist(p1: Point, p2: Point) -> float:
    return sqrt(
        (p2[0] - p1[0]) * (p2[0] - p1[0])
        + (p2[1] - p1[1]) * (p2[1] - p1[1])
        + (p2[2] - p1[2]) * (p2[2] - p1[2])
    )


ps: list[Point] = []
for line in input:
    x_str, y_str, z_str = line.split(",")
    ps.append((int(x_str), int(y_str), int(z_str)))

circuits = [set([i]) for i in range(len(ps))]
mem = dict((i, i) for i in range(len(ps)))

ds: list[tuple[int, int, float]] = []
for i1, i2 in combinations(range(len(ps)), 2):
    ds.append((i1, i2, dist(ps[i1], ps[i2])))

ds.sort(key=itemgetter(2))

for i in range(len(ds)):
    a, b, _ = ds[i]
    a_circ_i, b_circ_i = mem[a], mem[b]
    if a_circ_i == b_circ_i:
        continue

    circuits[a_circ_i] = circuits[a_circ_i].union(circuits[b_circ_i])
    if len(circuits[a_circ_i]) == len(ps):
        print(ps[a][0] * ps[b][0])
        break
    for j in circuits[b_circ_i]:
        mem[j] = a_circ_i
    circuits[b_circ_i].clear()
