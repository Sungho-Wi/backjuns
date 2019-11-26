a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)
value = [0 for i in range(10)]

for i in range(len(mul)):
    value[int(mul[i])] += 1

for i in value:
    print(i)