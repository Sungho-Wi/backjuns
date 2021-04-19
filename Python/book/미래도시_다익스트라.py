import heapq

N, M = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

X, K = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (N + 1)

    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        d, s = heapq.heappop(q)

        for g in graph[s]:
            if distance[g] > d + 1:
                heapq.heappush(q, (d + 1, g))
                distance[g] = d + 1

    return distance


result = dijkstra(1)[K] + dijkstra(K)[X]
print('-1' if result >= INF else result)
