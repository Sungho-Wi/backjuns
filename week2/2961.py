def gap(start, valueS, valueB, size):
    valueS = valueS * list1[start][0]
    valueB = valueB + list1[start][1]
    for i in range(start + 1, size):
        gap(i, valueS, valueB, size)
    global minGap

    if minGap > abs(valueS - valueB):
        minGap = abs(valueS - valueB)
        return

size = int(input())
if size < 1 or size > 10:
    exit()

list1 = []

for i in range(0, size):
     list1.append(list(map(int, input().split())))

minGap = 1000000000

for i in range(0, size):
    gap(i, 1, 0, size)

print(minGap)