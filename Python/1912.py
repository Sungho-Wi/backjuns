size = int(input())
line = list(map(int, input().split()))

result = []

plus = line[0]
result.append(plus)
for i in range(1, len(line)):
    if plus + line[i] >= line[i]:
        plus += line[i]
        result.append(plus)
    else:
        plus = line[i]
        result.append(plus)

print(max(result))