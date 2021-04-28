N, K = map(int, input().split())

graph = [[]]

virus_list = []
row = 1

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def set_virus(tuple_):
    index = tuple_[0]
    value = tuple_[1]

    value = int(value)

    if value != 0:
        virus_list.append((value, row, index + 1))

    return value


for _ in range(N):
    graph.append([0] + list(map(set_virus, enumerate(input().split()))))
    row += 1

virus_list.sort()
S, X, Y = map(int, input().split())

for t in range(S):
    new_virus_list = []
    for v_i, v_y, v_x in virus_list[:]:
        for i in range(4):
            move_y = v_y + d[i][0]
            move_x = v_x + d[i][1]

            if 0 < move_y <= N and 0 < move_x <= N and graph[move_y][move_x] == 0:
                graph[move_y][move_x] = v_i
                new_virus_list.append((v_i, move_y, move_x))

    virus_list = new_virus_list

print(graph[X][Y])
