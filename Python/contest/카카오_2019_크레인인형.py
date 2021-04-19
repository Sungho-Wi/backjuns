def solution(board, moves):
    answer = 0

    stack = []

    for move in moves:
        toy = 0
        for x in range(len(board)):
            if board[x][move-1] == 0:
                continue
            else:
                toy = board[x][move - 1]
                board[x][move - 1] = 0
                break

        if toy != 0:
            if stack and stack[-1] == toy:
                answer += 2
                stack.pop()
            else:
                stack.append(toy)


    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
