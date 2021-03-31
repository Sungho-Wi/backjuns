import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

X, Y = map(int, input().split())

graph = []

distance = [[INF] * X for _ in range(Y)]

for _ in range(Y):
    graph.append(list(map(int, list(input().rstrip()))))

def dijkstra():
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    q = []

    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0

    while q:
        dist, y, x = heapq.heappop(q)

        if distance[y][x] < dist:
            continue

        for i in range(4):
            y_ = y + dy[i]
            x_ = x + dx[i]

            if 0 <= y_ < Y and 0 <= x_ < X:
                cost = dist + graph[y_][x_]
                if distance[y_][x_] > cost:
                    distance[y_][x_] = cost
                    heapq.heappush(q, (cost, y_, x_))

dijkstra()

print(distance[Y-1][X-1])