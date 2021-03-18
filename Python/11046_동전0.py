N, K = map(int, input().split())

coin_list = []
coin_count = 0

for i in range(N):
    coin_list.append(int(input()))

for coin in reversed(coin_list):
    if K < coin:
        continue

    coin_count += K // coin
    K = K % coin

print(coin_count)
