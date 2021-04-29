n = int(input())

tree = []

for _ in range(n):
    tree.append(list(map(int, input().split())))

for i in range(1, n):
    for t_i, t_v in enumerate(tree[i]):
        max_value = 0
        if 0 <= t_i - 1:
            max_value = max(max_value, tree[i - 1][t_i - 1])
        if t_i < i:
            max_value = max(max_value, tree[i - 1][t_i])

        tree[i][t_i] = tree[i][t_i] + max_value

print(max(tree[n-1]))