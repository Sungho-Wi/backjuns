n, m = map(int, input().split(' '))

min_value = 0

for i in range(n):
    value = min(list(map(int, input().split())))

    min_value = max(min_value, value)
    # if min_value < value:
    #     min_value = value

print(min_value)