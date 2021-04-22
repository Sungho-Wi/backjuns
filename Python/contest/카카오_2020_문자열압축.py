def solution(string):
    # 문자열 길이가 1일때 런타임 에러 대응
    if len(string) == 1:
        return 1

    results = []

    for i in range(1, len(string) // 2 + 1):
        s = string[:]
        pattern = s[:i]
        repeated_count = 1

        k = i

        while k + i <= len(s):
            if pattern == s[k:k + i]:
                repeated_count += 1
            else:
                if repeated_count > 1:
                    de = f'{repeated_count}{pattern}'
                    s = s[:k - (i * repeated_count)] + de + s[k:]

                    k -= (i * repeated_count) - len(de)
                    repeated_count = 1

                pattern = s[k:k + i]

            k += i

        if repeated_count > 1:
            de = f'{repeated_count}{pattern}'
            s = s[:k - (i * repeated_count)] + de + s[k:]

        results.append(len(s))

    return min(results)


testcase = ["a"]

for t in testcase:
    print(solution(t))
