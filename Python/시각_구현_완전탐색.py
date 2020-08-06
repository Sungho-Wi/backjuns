import time

n = int(input())

count = 0

start = time.time()

# type 1
# 3중 for문 사용 무식한 완전탐색

# for h in range(n + 1):
#     if h == 3:
#         count += 3600
#         continue
#     else:
#         for m in range(60):
#             if m // 10 == 3 or m % 10 == 3:
#                 count += 60
#                 continue
#             else:
#                 for s in range(60):
#                     if s // 10 == 3 or s % 10 == 3:
#                         count += 1

# type 2
# 3중 for문을 1중 for문으로

# for h in range(n + 1):
#     if h == 3:
#         count += 3600
#         continue
#     else:
#         count += 1575

# type 3
# 1중 for문으로 단순 연산으로

if n + 1 > 3:
    count = (n * 1575) + 3600
else:
    count = ((n + 1) * 1575)

end = time.time()

print('소요시간 {}'.format(end - start))
print(count)