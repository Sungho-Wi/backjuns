a = int(input())

count = 2
for i in range(2, int(a/2)):
    if a % i == 0:
        print(i, end=" ")