import fileinput

input = map(str.rstrip, fileinput.input())

total = 0
for line in input:
    digits = [int(c) for c in line]
    batteries = [0 for _ in range(12)]
    loc = 0
    for level in range(12):
        order = 12 - 1 - level
        for i in range(loc, len(digits) - order):
            if digits[i] > batteries[level]:
                batteries[level] = digits[i]
                loc = i + 1

        total += (10**order) * batteries[level]

print(total)
