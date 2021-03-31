import sys

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())

start = int(input())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, V + 1):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for d in graph[start]:
        distance[d[0]] = d[1]

    for i in range(V - 1):
        now = get_smallest_node()

        for d in graph[now]:
            distance[d[0]] = min(distance[d[0]], distance[now] + d[1])

dijkstra(start)

print(distance)
