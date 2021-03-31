from collections import deque


def bfs(x, y, picture):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque([(x, y)])
    color = picture[y][x]
    picture[y][x] = 'V'

    while queue:
        x_, y_ = queue.popleft()
        for i in range(4):
            m_x = x_ + dx[i]
            m_y = y_ + dy[i]

            if 0 <= m_y < N and 0 <= m_x < N and picture[m_y][m_x] == color:
                queue.append((m_x, m_y))
                picture[m_y][m_x] = 'V'


N = int(input())

PICTURE = []
PICTURE_TWO = []

for _ in range(N):
    row = input()
    PICTURE.append(list(row))
    PICTURE_TWO.append(list(row.replace('G', 'R')))

result = 0

for Y in range(N):
    for X in range(N):
        if PICTURE[Y][X] != 'V':
            bfs(X, Y, PICTURE)
            result += 1

result_two = 0

for Y in range(N):
    for X in range(N):
        if PICTURE_TWO[Y][X] != 'V':
            bfs(X, Y, PICTURE_TWO)
            result_two += 1

print(result, result_two)
