n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for k in range(1, n + 1):
    graph[k][k] = 0

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a][b] = min(graph[a][b], c)

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

for i in range(1, n + 1):
    for k in range(1, n + 1):
        if graph[i][k] == INF:
            print('0', end=' ')
        else:
            print(graph[i][k], end=' ')
    print(end='\n')
