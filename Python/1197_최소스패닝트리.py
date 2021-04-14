def find_parend(parent, x):
    if parent[x] != x:
        parent[x] = find_parend(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parend(parent, a)
    b = find_parend(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())

edges = []
parent = [i for i in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort(key=lambda x: x[0])
result = 0

for c, a, b in edges:
    if find_parend(parent, a) != find_parend(parent, b):
        union_parent(parent, a, b)
        result += c

print(result)
