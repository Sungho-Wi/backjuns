import copy


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret


def check_key(lock, key, y, x, start, end):
    for y_ in range(len(key)):
        for x_ in range(len(key)):
            lock[y + y_][x + x_] += key[y_][x_]

    for y_ in range(start, end):
        for x_ in range(start, end):
            if lock[y_][x_] != 1:
                return False

    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)

    length = (((M - 1) * 2) + N)

    lock = [[0] * length for _ in range(M - 1)] + list(map(lambda x: ([0] * (M - 1)) + x + ([0] * (M - 1)), lock)) + [
        [0] * length for _ in range(M - 1)]

    for i in range(4):
        for a in range(M + N - 1):
            for b in range(M + N - 1):
                if check_key(copy.deepcopy(lock), key, a, b, M - 1, M + N - 1):
                    return True
        key = rotate_90(key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
