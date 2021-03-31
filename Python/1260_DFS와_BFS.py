from collections import deque

N, M, V = map(int, input().split())

graph = {}

visited = [False] * (N + 1)

for _ in range(M):
    first, second = map(int, input().split())
    if first not in graph:
        graph[first] = [second]
    else:
        graph[first].append(second)
    if second not in graph:
        graph[second] = [first]
    else:
        graph[second].append(first)


for index, value in graph.items():
    graph[index] = sorted(value)


def dfs(graph_, index, visited_):
    print(index, end=' ')
    visited_[index] = True

    if index in graph:
        for i in graph_[index]:
            if not visited_[i]:
                dfs(graph_, i, visited_)


dfs(graph, V, visited)

print(end='\n')
visited = [False] * (N + 1)


def bfs(queue: deque, graph_, visited_):
    while queue:
        i = queue.popleft()
        print(i, end=' ')
        if i in graph_:
            for index in graph_[i]:
                if not visited_[index]:
                    visited_[index] = True
                    queue.append(index)

visited[V] = True
bfs(deque([V]), graph, visited)
