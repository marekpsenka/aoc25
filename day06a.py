import fileinput
from math import prod

input = list(fileinput.input())

op_loc = list(filter(lambda p: p[1] != " ", enumerate(input[-1])))

total = 0
for i in range(len(op_loc)):
    left, op = op_loc[i]
    if i == len(op_loc) - 1:
        right = len(input[0]) - 1
    else:
        right = op_loc[i + 1][0] - 1

    numbers = [int(input[j][left:right]) for j in range(len(input) - 1)]
    if op == "+":
        total += sum(numbers)
    else:
        total += prod(numbers)

print(total)
