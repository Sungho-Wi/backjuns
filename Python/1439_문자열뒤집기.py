s = list(input())

results = [s[0]]

for c in s:
    if results[-1] != c:
        results.append(c)

print(min(results.count('0'), results.count('1')))
