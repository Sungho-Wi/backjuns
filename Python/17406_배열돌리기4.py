from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())

MATRIX = [[0]]

op_list = []

for _ in range(N):
    MATRIX.append([0] + list(map(int, input().split())))

for _ in range(K):
    op_list.append(list(map(int, input().split())))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

result = int(1e9)

for k in permutations(range(len(op_list)), len(op_list)):
    matrix = deepcopy(MATRIX)
    for i in k:
        a, b, c = op_list[i]
        top = a - c
        right = b + c
        left = b - c
        bottom = a + c

        middle = (top + ((bottom - top) // 2), left + ((right - left) // 2))

        temp = matrix[top][left]

        y = top
        x = left + 1
        cur_d = 0

        while not (top == middle[0] and left == middle[1]):
            matrix[y][x], temp = temp, matrix[y][x]

            if y in (top, bottom) and x in (left, right):
                if y == top and x == left:
                    top += 1
                    left += 1
                    right -= 1
                    bottom -= 1
                    y = top
                    x = left + 1
                    temp = matrix[top][left]
                    cur_d = 0
                    continue

                cur_d += 1

            y += d[cur_d][0]
            x += d[cur_d][1]

    for row in range(1, len(matrix)):
        result = min(result, sum(matrix[row]))

print(result)
