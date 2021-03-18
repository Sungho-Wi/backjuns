from functools import reduce

N = int(input())

word_list = []

for i in range(N):
    word_list.append(input())

curr_max_number = 9

alphabet_dict = {}

for word in word_list:
    for index, alphabet in enumerate(reversed(word)):
        value = 10 ** index
        if alphabet_dict.get(alphabet) is None:
            alphabet_dict[alphabet] = value
        else:
            alphabet_dict[alphabet] += value

sorted_list = sorted(alphabet_dict.items(), key=lambda x:x[1], reverse=True)

alphabet_result = {}
max_value = 9

for item in sorted_list:
    alphabet_result[item[0]] = str(max_value)
    max_value -= 1

result_score = 0

for word in word_list:
    score = ''
    for alphabet in word:
        score += alphabet_result[alphabet]

    result_score += int(score)

print(result_score)



