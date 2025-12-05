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

ranges.sort(key=lambda range: range.left)

i = 0
total = 0
while i < len(ranges):
    j = i + 1
    maximal = ranges[i].right
    while j < len(ranges):
        if ranges[j].left <= maximal:
            if maximal < ranges[j].right:
                maximal = ranges[j].right
            j += 1
        else:
            break
    total += maximal - ranges[i].left + 1
    i = j


print(total)
