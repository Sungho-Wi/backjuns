from itertools import permutations

N = int(input())

values = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

operators = []
operators += [0] * a
operators += [1] * b
operators += [2] * c
operators += [3] * d

min_value = int(1e9)
max_value = -int(1e9)

for items in set(permutations(operators, len(values) - 1)):
    result = values[0]
    for i in range(len(items)):
        if items[i] == 0:
            result += values[i + 1]
        elif items[i] == 1:
            result -= values[i + 1]
        elif items[i] == 2:
            result *= values[i + 1]
        elif items[i] == 3:
            result = int(result / values[i + 1])

    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)
