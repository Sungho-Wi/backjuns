from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    map_ = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, list(input().split()))
        map_[Y][X] = True


    def check_home(y_, x_, queue):
        if 0 <= y_ < N and 0 <= x_ < M:
            if map_[y_][x_] == 1:
                map_[y_][x_] = 2
                queue.append((y_, x_))


    def get_count(y_, x_):
        queue = deque([(y_, x_)])

        while queue:
            y, x = queue.popleft()

            map_[y][x] = 2

            check_home(y - 1, x, queue)
            check_home(y + 1, x, queue)
            check_home(y, x - 1, queue)
            check_home(y, x + 1, queue)


    count = 0

    for y in range(N):
        for x in range(M):
            if map_[y][x] == 1:
                get_count(y, x)
                count += 1

    print(count)
