import heapq

N, M, C = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    X, Y, Z = map(int, input().split())

    graph[X].append((Z, Y))


def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        d, s = heapq.heappop(q)

        if distance[s] < d:
            continue

        for d_, s_ in graph[s]:
            time = d + d_
            if time < distance[s_]:
                heapq.heappush(q, (time, s_))
                distance[s_] = time

    return distance

result = 0
count = 0

for value in dijkstra(C):
    if value == INF or value == 0:
        continue

    result = max(result, value)
    count += 1

print(count, result)

