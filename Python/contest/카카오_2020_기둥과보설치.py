def check(result):
    for x, y, a in result:
        # 기둥
        # 1. 바닥 위에 있어야댐
        # 2. 보의 한쪽 끝 부분 위에 있어야댐
        # 3. 다른 기둥 위에 있어야댐
        if a == 0:
            if y == 0 or (x, y - 1, 0) in result or (x - 1, y, 1) in result or (x, y, 1) in result:
                continue
            else:
                return False
        # 보
        # 1. 한쪽 끝 부분이 기둥 위에 있어야댐
        # 2. 양쪽 끝 부분이 다른 보와 동시에 연결
        else:
            if (x, y - 1, 0) in result or (x + 1, y - 1, 0) in result or ((x - 1, y, 1) in result and (x + 1, y, 1) in result):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    result = []

    for x, y, a, b in build_frame:
        if b == 1:
            result.append((x, y, a))
        else:
            result.remove((x, y, a))

        if not check(result):
            if b == 1:
                result.remove((x, y, a))
            else:
                result.append((x, y, a))

    return sorted(result)

print(sorted(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])))