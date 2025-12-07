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
multiplicity: dict[Point, int] = dict()
start: Point | None = None

for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
        elif c == "^":
            splitters[j].append(i)
            multiplicity[(i, j)] = 0

assert start is not None
first = first_larger(splitters[start[1]], start[0])
assert first is not None
multiplicity[(first, start[1])] += 1

total = 0

for s_i, s_j in multiplicity.keys():
    mult = multiplicity[(s_i, s_j)]
    if mult == 0:
        continue
    if s_j < len(input[0]) - 1:
        match first_larger(splitters[s_j + 1], s_i):
            case None:
                total += mult
            case int() as i:
                multiplicity[(i, s_j + 1)] += mult
    if s_j > 0:
        match first_larger(splitters[s_j - 1], s_i):
            case None:
                total += mult
            case int() as i:
                multiplicity[(i, s_j - 1)] += mult

print(total)
