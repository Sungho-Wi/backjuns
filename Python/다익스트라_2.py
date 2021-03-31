import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

정점개수, 간선개수 = map(int, input().split())
start = int(input())

graph = [[] for _ in range(정점개수 + 1)]
distance = [INF] * (정점개수 + 1)

for _ in range(간선개수):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for d in graph[now]:
            cost = distance[now] + d[1]
            if cost < distance[d[0]]:
                distance[d[0]] = cost
                heapq.heappush(q, (cost, d[0]))

dijkstra(start)

print(distance)
