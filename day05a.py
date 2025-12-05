import fileinput
from dataclasses import dataclass
from itertools import takewhile


@dataclass
class Range:
    left: int
    right: int

    def contains(self, n: int) -> bool:
        return n >= self.left and n <= self.right


input = map(str.rstrip, fileinput.input())

range_strs = takewhile(lambda s: s, input)
ranges: list[Range] = list()
for range_str in range_strs:
    left_str, right_str = range_str.split("-")
    ranges.append(Range(int(left_str), int(right_str)))

fresh = 0
for line in input:
    if any(map(lambda range: range.contains(int(line)), ranges)):
        fresh += 1

print(fresh)
