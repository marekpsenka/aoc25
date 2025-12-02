import fileinput

input = map(str.rstrip, fileinput.input())


def rotate(pos: int, rot_str: str) -> tuple[int, int]:
    zero_count = 0
    rotation = int(rot_str[1:])
    if rot_str[0] == "L":
        new_pos = pos - rotation
        if new_pos <= 0:
            if pos == 0:
                zero_count += rotation // 100
            else:
                zero_count += 1 + (-new_pos) // 100

    elif rot_str[0] == "R":
        new_pos = pos + rotation
        if new_pos >= 100:
            zero_count += new_pos // 100
    else:
        raise RuntimeError

    return new_pos % 100, zero_count


pos = 50
total_zero_count = 0
for line in input:
    pos, clicks = rotate(pos, line)
    total_zero_count += clicks

print(total_zero_count)

assert rotate(50, "R1000") == (50, 10)
assert rotate(50, "L100") == (50, 1)
assert rotate(50, "L1000") == (50, 10)
assert rotate(0, "L100") == (0, 1)
assert rotate(0, "L1") == (99, 0)
assert rotate(3, "L4") == (99, 1)
assert rotate(99, "R1") == (0, 1)
assert rotate(99, "R100") == (99, 1)
assert rotate(0, "R100") == (0, 1)
assert rotate(0, "L99") == (1, 0)
assert rotate(50, "L50") == (0, 1)
assert rotate(50, "R50") == (0, 1)
assert rotate(0, "L101") == (99, 1)
