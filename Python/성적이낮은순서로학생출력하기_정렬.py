n = int(input())

list = []
for i in range(n):
    name, score = input().split(' ')
    list.append((name, int(score)))

sorted_list = sorted(list, key=lambda x: x[1])

for k in sorted_list:
    print(k[0], end=' ')