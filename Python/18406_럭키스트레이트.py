N = input()

half = len(N) // 2

if sum(map(int, N[:half])) == sum(map(int, N[half:])):
    print('LUCKY')
else:
    print('READY')
