n, m, k = map(int, input().split(' '))
list = list(map(int, input().split(' ')))

list.sort(reverse=True)

value = 0
i = 0

while i < m:
    for a in range(k):
        value += list[0]
        i += 1

    value += list[1]
    i += 1

print(value)

print((m // (k + 1)) * k)


# 단순 연산으로 구하는 식
count = m // (k + 1)
value = ((list[0] * k) + list[1]) * count
value += list[0] * (m % (k + 1))

print(value)
