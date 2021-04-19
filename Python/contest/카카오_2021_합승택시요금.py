import heapq

INF = int(1e9)

"""
플로이드 워셜 방법으로 풀어볼 것
"""


def dijkstra(n, s, graph):
    q = []

    heapq.heappush(q, (0, s))
    distance = [INF] * (n + 1)
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for d in graph[now]:
            cost = distance[now] + d[1]
            if cost < distance[d[0]]:
                distance[d[0]] = cost
                heapq.heappush(q, (cost, d[0]))

    return distance


def solution(n, s, a, b, fares):
    answer = INF

    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))

    distance = dijkstra(n, s, graph)

    for i in range(1, n + 1):
        result = dijkstra(n, i, graph)
        answer = min(answer, distance[i] + result[a] + result[b])

    return answer


print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
