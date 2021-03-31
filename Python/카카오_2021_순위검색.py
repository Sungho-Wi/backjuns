from itertools import product
import bisect


def get_count(score, score_list):
    return len(score_list) - bisect.bisect_left(score_list, score)


def solution(info, query):
    answer = []

    types = list(product([False, True], repeat=4))

    score_dict = {}

    for info_str in info:
        info_list = info_str.split()
        score = int(info_list[4])
        info_list = info_list[:-1]

        for type_ in types:
            key_str = ''
            for idx, bo in enumerate(type_):
                if bo:
                    key_str += info_list[idx]
                else:
                    key_str += '-'

            if key_str in score_dict.keys():
                score_dict[key_str].append(score)
            else:
                score_dict[key_str] = [score]

    for key in score_dict.keys():
        score_dict[key].sort()

    for query_str in query:
        query_str = query_str.replace('and', '')
        query_list = query_str.split()
        score = int(query_list[-1])
        query_str = ''.join(query_list[:-1])

        if query_str in score_dict.keys():
            answer.append(get_count(score, score_dict[query_str]))
        else:
            answer.append(0)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
