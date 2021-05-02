T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    matrix = [[0 for _ in range(m)] for _ in range(n)]

    dp = [[0 for _ in range(m)] for _ in range(n)]

    for index, v in enumerate(map(int, input().split())):
        matrix[index // m][index % m] = v

    for i in range(n):
        dp[i][0] = matrix[i][0]

    for x in range(1, m):
        for y in range(n):
            max_pre_value = 0
            for d in (-1, 0, 1):
                if not 0 <= y + d < n:
                    continue
                max_pre_value = max(max_pre_value, dp[y + d][x - 1])

            dp[y][x] = matrix[y][x] + max_pre_value

    results = []
    for i in range(n):
        results.append(dp[i][m - 1])

    print(max(results))