import fileinput

input = map(str.rstrip, fileinput.input())

total = 0
for line in input:
    digits = [int(c) for c in line]
    first = 0
    first_loc = 0
    second = 0
    for i in range(len(digits) - 1):
        if digits[i] > first:
            first = digits[i]
            first_loc = i
    for j in range(first_loc + 1, len(digits)):
        if digits[j] > second:
            second = digits[j]

    total += 10 * first + second

print(total)
