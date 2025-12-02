import fileinput

input = map(str.rstrip, fileinput.input())

pos = 50
zero_count = 0
for line in input:
    if line[0] == "L":
        pos = pos - int(line[1:]) % 100
    elif line[0] == "R":
        pos = (pos + int(line[1:])) % 100
    else:
        raise RuntimeError

    if pos == 0:
        zero_count += 1

print(zero_count)
