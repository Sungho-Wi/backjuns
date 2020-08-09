n, m = map(int, input().split())
array = list(map(int, input().split()))

print(array)

left = 0
right = max(array)

result = 0

while left <= right:
    half = (left + right) // 2

    total = 0
    for i in array:
        if half < i:
            total += i - half

    # 떡의 양이 부족한 경우 더 많이 자르기
    if total < m:
        right = half - 1
    # 떡의 양이 충분한 경우 결과에 저장하고 덜 자르기
    else:
        result = half
        left = half + 1

print(result)
