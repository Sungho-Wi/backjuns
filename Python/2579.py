size = int(input())

W = [0]
for i in range(size):
    W.append(int(input()))

DP = [0]
DP.append(W[1])
DP.append(W[1] + W[2])

for n in range(3, size+1):
    if DP[n-2] + W[n] <= DP[n-3] + W[n-1] + W[n]:
        DP.append(DP[n-3] + W[n-1] + W[n])
    else:
        DP.append(DP[n-2] + W[n])

print(DP[-1])