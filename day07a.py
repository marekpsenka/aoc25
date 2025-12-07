import fileinput
from collections import defaultdict

Point = tuple[int, int]


def first_larger(ss: list[int], i: int) -> int | None:
    for j in ss:
        if j > i:
            return j
    return None


input = list(map(str.rstrip, fileinput.input()))
splitters: defaultdict[int, list[int]] = defaultdict(list)
queue: list[Point] = []

for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c == "S":
            queue.append((i, j))
        elif c == "^":
            splitters[j].append(i)

hit: set[Point] = set()

while len(queue) > 0:
    o_i, o_j = queue.pop()
    match first_larger(splitters[o_j], o_i):
        case None:
            continue
        case int() as i:
            if (i, o_j) in hit:
                continue
            if o_j < len(input[0]) - 1:
                queue.append((i, o_j + 1))
            if o_j > 1:
                queue.append((i, o_j - 1))
            hit.add((i, o_j))

print(len(hit))
