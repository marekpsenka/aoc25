import fileinput


def neighbors_8(
    i: int, j: int, max_i: int, max_j: int
) -> list[tuple[int, int]]:
    if i == 0:
        if j == 0:
            return [(1, 0), (0, 1), (1, 1)]

        if j == max_j - 1:
            return [(1, max_j - 1), (0, max_j - 2), (1, max_j - 2)]

        return [(0, j - 1), (1, j - 1), (1, j), (0, j + 1), (1, j + 1)]

    if i == max_i - 1:
        if j == max_j - 1:
            return [
                (max_i - 2, max_j - 1),
                (max_i - 1, max_j - 2),
                (max_i - 2, max_j - 2),
            ]

        if j == 0:
            return [(max_i - 1, 1), (max_i - 2, 0), (max_i - 2, 1)]

        return [
            (max_i - 1, j - 1),
            (max_i - 2, j - 1),
            (max_i - 2, j),
            (max_i - 2, j + 1),
            (max_i - 1, j + 1),
        ]

    if j == 0:
        return [(i - 1, 0), (i - 1, 1), (i, 1), (i + 1, 0), (i + 1, 1)]

    if j == max_j - 1:
        return [
            (i - 1, max_j - 1),
            (i - 1, max_j - 2),
            (i, max_j - 2),
            (i + 1, max_j - 2),
            (i + 1, max_j - 1),
        ]

    return [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]


input = list(map(str.rstrip, fileinput.input()))

max_i = len(input)
max_j = len(input[0])

accessible = 0
for i in range(max_i):
    for j in range(max_j):
        if input[i][j] != "@":
            continue
        items = map(
            lambda p: input[p[0]][p[1]], neighbors_8(i, j, max_i, max_j)
        )

        num_rolls = sum(1 for _ in filter(lambda c: c == "@", items))
        if num_rolls < 4:
            accessible += 1

print(accessible)
