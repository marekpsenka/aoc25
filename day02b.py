import fileinput
from dataclasses import dataclass


@dataclass
class Range:
    left: int
    right: int

    def contains(self, n: int) -> bool:
        return n >= self.left and n <= self.right


input = map(str.rstrip, fileinput.input())
ranges: list[Range] = []
for range_str in next(input).split(","):
    left_str, right_str = range_str.split("-")
    ranges.append(Range(int(left_str), int(right_str)))

ranges.sort(key=lambda range: range.left)

found: set[int] = set()
for seed in range(1, 100000):
    id_str = 2 * str(seed)
    id = int(id_str)
    while id < 10000000000:
        for range in ranges:
            if range.contains(id) and id not in found:
                found.add(id)
                break
        id_str += str(seed)
        id = int(id_str)

print(sum(found))
