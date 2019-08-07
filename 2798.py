size, maxi = map(int, input().split())
card = list(map(int, input().split()))

result = []
def serch(num, value, count):
    if count + 1 == 3:
        if maxi >= value + card[num]:
            result.append(value + card[num])
        return
    for i in range(num + 1, len(card)):
        serch(i, value + card[num], count + 1)


for j in range(len(card)):
    serch(j, 0, 0)

result2 = []
for k in range(len(result)):
    result2.append(abs(maxi - result[k]))

mins = min(result2)
print(result[result2.index(mins)])