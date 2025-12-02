import fileinput

input = map(str.rstrip, fileinput.input())

total = 0
for range_str in next(input).split(","):
    sub_total = 0
    left_str, right_str = range_str.split("-")
    left, right = int(left_str), int(right_str)
    if len(left_str) == 1:
        pali_half = 1
    else:
        pali_half = int(left_str[: (len(left_str) // 2)])
    while True:
        pali = max(int(str(pali_half) + str(pali_half)), 1)
        if pali > right:
            break
        pali_half += 1
        if pali >= left:
            sub_total += pali
    total += sub_total

print(total)
