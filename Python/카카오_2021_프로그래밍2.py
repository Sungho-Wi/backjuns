def find(order, index, curr_num, max_num):
    if curr_num == max_num:
        return [order[index]]

    str_list = []

    for i in range(index, len(order)):
        if max_num - curr_num > (len(order) - 1) - i:
            break
        find_values = find(order, i + 1, curr_num + 1, max_num)
        for find_value in find_values:
            str_list.append(order[index] + find_value)

    return str_list


def solution(orders, course):
    answer = []

    dic = {}

    for num in course:
        dic_num = {}
        for order in orders:
            for i in range(len(order)):
                if num + i > len(order):
                    break
                find_list = find(order, i, 1, num)
                for value in find_list:
                    value = sorted(value)
                    value_str = ''.join(value)
                    if value_str in dic_num.keys():
                        dic_num[value_str] += 1
                    else:
                        dic_num[value_str] = 1

        max_value = max(dic_num.values()) if len(dic_num) > 0 else 0
        for dic_key in dic_num.keys():
            if dic_num[dic_key] == max_value:
                dic[dic_key] = dic_num[dic_key]

    for dic_key in dic.keys():
        if dic[dic_key] > 1:
            answer.append(dic_key)

    return sorted(answer)