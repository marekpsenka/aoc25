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

adj = [[0 for _ in range(len(ps))] for _ in range(len(ps))]

ds: list[tuple[int, int, float]] = []
for i1, i2 in combinations(range(len(ps)), 2):
    ds.append((i1, i2, dist(ps[i1], ps[i2])))

ds.sort(key=itemgetter(2))

for i in range(1000):
    a, b, _ = ds[i]
    adj[a][b] = 1
    adj[b][a] = 1

visited: set[int] = set()
sizes: list[int] = []


def dfs(dest: int, visited: set[int]) -> int:
    if dest in visited:
        return 0
    size = 1
    visited.add(dest)
    for i in range(len(adj[dest])):
        if adj[dest][i] == 1:
            size += dfs(i, visited)
    return size


for i in range(len(adj)):
    if i in visited:
        continue
    component: set[int] = set()
    sizes.append(dfs(i, component))
    visited = visited.union(component)

sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
