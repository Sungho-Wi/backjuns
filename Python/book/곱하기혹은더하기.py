nums = list(map(int, list(input())))

result = 0

for n in nums:
    result = max(result + n, result * n)

print(result)
