"""
불필요한 간선은 없애고 유지비가 가장 적게 드는 도로를 사이클이 없게 만들어야 하므로
신장트리 이면서 최소한의 비용을 구하는 크루스칼 알고리즘으로 구현

마을을 두개 만들어야 하므로 신장트리에서 간선 하나를 없앨 시 두개의 신장트리가 만들어짐
최대 비용의 간선을 제거하면 최소한의 비용이 듦
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(N + 1)]

result = 0
max_value = 0

for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        max_value = max(max_value, c)

print(result - max_value)
