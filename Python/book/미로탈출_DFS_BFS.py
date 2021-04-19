from collections import deque

n, m = map(int, input().split(' '))

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS

# def escape(graph, x, y):
#     if x >= m or x < 0 or y >= n or y < 0:
#         return 999999
#
#     if graph[y][x] == 0:
#         return 999999
#
#     if x == (m - 1) and y == (n - 1):
#         return 1
#
#     graph[y][x] = 0
#
#     result = 1
#
#     result += min(escape(graph, x + 1, y), escape(graph, x - 1, y), escape(graph, x, y + 1), escape(graph, x, y - 1))
#
#     return result

# print(escape(graph, 0, 0))

# BFS


def bfs(graph):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            dy = y + direction[d][0]
            dx = x + direction[d][1]

            if dy < 0 or dy >= n or dx < 0 or dx >= m:
                continue

            if graph[dy][dx] == 0:
                continue

            if graph[dy][dx] == 1:
                queue.append((dy, dx))
                graph[dy][dx] = graph[y][x] + 1

    print(graph[n - 1][m - 1])


bfs(graph)
