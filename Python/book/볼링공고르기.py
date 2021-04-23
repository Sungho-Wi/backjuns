"""
O(n^2)

N, M = map(int, input().split())
ball_list = list(map(int, input().split()))

count = 0

for i in range(len(ball_list)):
    for k in range(i + 1, len(ball_list)):
        if ball_list[i] != ball_list[k]:
            count += 1

print(count)
"""

N, M = map(int, input().split())
ball_list = list(map(int, input().split()))
count_list = [0 for _ in range(N + 1)]

for b in ball_list:
    count_list[b] += 1

result = 0

for i in range(1, len(count_list)):
    k = count_list[i]
    result += k * (N - k)
    N -= k

print(result)
