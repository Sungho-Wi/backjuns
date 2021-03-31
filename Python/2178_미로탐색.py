from collections import deque

N, M = map(int, input().split())

GRAPH = []

for _ in range(N):
    GRAPH.append(list(map(lambda a: a == '1', list(input()))))


def bfs(queue, graph):
    while queue:
        x, y, count = queue.popleft()

        if x == M - 1 and y == N - 1:
            return count

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]

            if 0 <= x_ < M and 0 <= y_ < N and graph[y_][x_]:
                graph[y_][x_] = False
                queue.append((x_, y_, count + 1))


GRAPH[0][0] = False
print(bfs(deque([(0, 0, 1)]), GRAPH))
