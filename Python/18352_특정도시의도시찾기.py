from collections import deque

N, M, K, X = map(int, input().split())

INF = int(1e9)

roads = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    roads[a].append(b)

distance = [INF for _ in range(N + 1)]

queue = deque([])
queue.append((X, 0))
distance[X] = 0

while queue:
    n, d = queue.popleft()

    for k in roads[n]:
        if distance[k] > d + 1:
            queue.append((k, d + 1))
            distance[k] = d + 1

results = list(map(str, filter(lambda i:distance[i] == K, range(1, len(distance)))))

if results:
    print('\n'.join(results))
else:
    print('-1')
