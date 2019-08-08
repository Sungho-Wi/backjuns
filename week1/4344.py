size = int(input())

value = list()

for i in range(0, size):
    sum = 0
    a = list(map(int, input().split()))
    for j in range(1, a[0]+1):
        sum += a[j]
    avg = sum / a[0]
    count = 0
    for j in range(1, a[0]+1):
        if a[j] > avg:
            count = count + 1
    value.append(float(count / a[0] * 100))

for i in range(0, len(value)):
    print("%0.3f" %(value[i]) + "%")
