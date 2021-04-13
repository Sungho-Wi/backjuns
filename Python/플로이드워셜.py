INF = int(1e9)

노드개수 = int(input())
간선개수 = int(input())

graph = [[INF] * (노드개수 + 1) for _ in range(노드개수 + 1)]

for i in range(1, 노드개수 + 1):
    graph[i][i] = 0

for _ in range(간선개수):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, 노드개수 + 1):
    for a in range(1, 노드개수 + 1):
        for b in range(1, 노드개수 + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
