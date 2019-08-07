number = int(input())

man = []
for i in range(number):
    man.append(list(map(int, input().split())))

result = []

for i in range(number):
    count = 1
    for j in range(number):
        if i == j:
            continue
        if man[j][0] > man[i][0] and man[j][1] > man[i][1]:
            count += 1
    result.append(str(count))

print(" ".join(result))