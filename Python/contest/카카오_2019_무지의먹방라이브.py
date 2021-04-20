# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    hq = []

    for i, f in enumerate(food_times):
        heapq.heappush(hq, (f, i + 1))

    pre_time = 0  # 직전에 다 먹은 음식 시간

    while True:
        f, i = hq[0]
        hq_len = len(hq)

        if f == pre_time:
            heapq.heappop(hq)
            continue

        passed_count = (f - pre_time) * hq_len
        pre_time = f

        if k <= passed_count:
            break

        k -= passed_count
        heapq.heappop(hq)

    hq.sort(key=lambda x: x[1])

    return hq[k % len(hq)][1]

