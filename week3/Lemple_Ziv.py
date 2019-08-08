#incoding
context = list(input())

dic = {}
result = []
skip = 0

for i in range(len(context)):
    if skip > 0:
        skip -= 1
        continue
    if context[i] not in dic: # 딕셔너리에 문자가 없다면
        result.append([0, 0, context[i]])
        dic[context[i]] = i
    else: #문자가 있다면
        pre = dic[context[i]] #딕셔너리에 인덱스값 저장
        count = 0
        for j in range(len(context)):
            if i + j >= len(context): # 패턴이 데이터 마지막까지 갔을경우
                result.append([i - pre, count, context[-1]])
                skip += 2
                break
            if context[pre + j] == context[i + j]: #계속 비교
                count += 1
                continue
            else:# 더이상 패턴이 아닌수가 나올경우
                result.append([i - pre, count, context[i+j]]) # 안곂치면 결과값 저장
                skip += count #스킵은 패턴이 나온만큼만 데이터 비교를 하지않음
                break

#출력
for k in result:
    if k[2] == '*':
        print('*0', end='')
        continue
    if k[0] == 0 or k[1] == 0:
        print(k[2], end='')
    else:
        print('*' + str(k[0]) + str(k[1]) + k[2], end='')

#decoding

context = list(input())

skip = 0
for i in range(len(context)):
    if skip > 0:
        skip -= 1
        continue
    if context[i] == '*':
        if context[i+1] < context[i+2]:
            skip += 2
            for j in range(int(context[i+2])):
                for k in range(int(context[i+1])):
                    print(context[i+k - (int(context[i+1]))], end='')
    print(context[i], end='')


