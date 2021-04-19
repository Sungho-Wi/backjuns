#  중위표기식 -> 후위표기식 -> 계산

#  ord(value) : 문자 value를 아스키코드로
#  chr(value) : 아스키코드 value를 문자로
value = input()

op = []
result = []


def level(c):
    if c == '+' or c == '-':
        return 0
    elif c == '*' or c == '/':
        return 1
    else:
        return 2


# 중위 -> 후위표기식 변환
for c in value:
    if '0' <= c <= '9':
        result.append(int(c))
    else:
        if c == ')':
            while True:
                pop_value = op.pop()
                if pop_value == '(':
                    break
                else:
                    result.append(pop_value)
            continue

        if len(op) == 0:
            op.append(c)
        elif level(op[len(op) - 1]) <= level(c):
            op.append(c)
        else:
            if op[len(op) - 1] == '(':
                op.append(c)
                continue
            result.append(op.pop())
            op.append(c)

for i in range(len(op)):
    result.append(op.pop())

print(result)

#  후위표기식 계산
num_list = []
op_result = 0

for c in result:
    if type(c) == int:
        num_list.append(c)
    else:
        value1 = num_list.pop()
        value2 = num_list.pop()

        if c == '+':
            num_list.append(value2 + value1)
        elif c == '-':
            num_list.append(value2 - value1)
        elif c == '*':
            num_list.append(value2 * value1)
        elif c == '/':
            num_list.append(value2 / value1)

for i in num_list:
    op_result += i

print(op_result)