from collections import deque

N = int(input())
D = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(D):
    first, second = map(int, input().split())

    graph[first].append(second)
    graph[second].append(first)

queue = deque([1])
visited[1] = True
count = 0

while queue:
    i = queue.popleft()

    for v in graph[i]:
        if not visited[v]:
            visited[v] = True
            count += 1
            queue.append(v)

print(count)
