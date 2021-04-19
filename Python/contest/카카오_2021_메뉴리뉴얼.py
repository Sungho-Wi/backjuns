import collections
from itertools import combinations


def solution(orders, course):
    answer = []

    for num in course:
        combined_list = []
        for order in orders:
            combined_list += combinations(sorted(order), num)

        most_ordered = collections.Counter(combined_list).most_common()
        for order_tuple in most_ordered:
            if order_tuple[1] > 1 and  most_ordered[0][1] == order_tuple[1]:
                answer.append(''.join(order_tuple[0]))

    return sorted(answer)


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
