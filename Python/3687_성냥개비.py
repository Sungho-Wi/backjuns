test_case_count = int(input())

test_list = []

for _ in range(test_case_count):
    test_list.append(int(input()))

min_values = [[0], [0], [1], [7], [4], [2, 3, 5], [0, 6, 9], [8]]
"""
8 10    2 + 6
9 18    2 + 7
10 22   5 + 5
11 20   5 + 6
12 28   5 + 7
13 68   6 + 7
14 88   7 + 7
15 108  2 + 6 + 7

"""
dp = [(0, 0), (0, 0), (1, 1), (7, 7), (4, 11), (2, 71), (6, 111), (8, 711), (10, 1111)]


def find_min_value(value):
    results_list = []
    for n in range(2, 8):
        dp_str = str(dp[value - n][0])
        min_str = str(min(min_values[n]))
        if n == 6:
            results_list.append(int(dp_str + min_str))
        else:
            results_list.append(int(dp_str + min_str))
            results_list.append(int(min_str + dp_str))

    return min(results_list)


for i in range(9, max(test_list) + 1):
    max_value = dp[i - 2][1] * 10 + 1
    min_value = find_min_value(i)

    dp.append((min_value, max_value))

for t in test_list:
    print(dp[t][0], dp[t][1])
