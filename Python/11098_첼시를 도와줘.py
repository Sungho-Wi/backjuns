N = int(input())
expensive_players = []

for i in range(N):
    P = int(input())
    expensive_player = [0, '']
    for k in range(P):
        player_info = input().split()
        player_value = int(player_info[0])
        player_name = player_info[1]

        if expensive_player[0] < player_value:
            expensive_player = [player_value, player_name]

    expensive_players.append(expensive_player[1])

for player in expensive_players:
    print(player)