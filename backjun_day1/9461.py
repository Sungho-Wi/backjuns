size = int(input())

P = [0, 1, 1, 1]
value = []
for i in range(size):
    value.append(int(input()))

# n-3 + n-2
for k in range(4, max(value) + 1):
    P.append(P[k-3] + P[k-2])

for j in value:
    print(P[j])
