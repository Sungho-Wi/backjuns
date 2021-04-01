def transfer_time_to_second(time_str):
    h, m, s = map(int, time_str.split(':'))

    h *= 60 * 60
    m *= 60

    return h + m + s


def transfer_second_to_time(second):
    h = second // (60 * 60)
    second -= 60 * 60 * h
    m = second // 60
    second -= 60 * m

    return f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(second).zfill(2)}'


def solution(play_time, adv_time, logs):
    answer = 0

    play_time = transfer_time_to_second(play_time)
    adv_time = transfer_time_to_second(adv_time)

    dp = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split('-')
        start = transfer_time_to_second(start)
        end = transfer_time_to_second(end)

        dp[start] += 1
        dp[end] -= 1

    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] + dp[i]

    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] + dp[i]

    dp_count = 1
    max_value = 0

    # 0번째 대응
    sum_value = dp[adv_time]
    if sum_value > max_value:
        max_value = sum_value
        answer = 0

    while dp_count + adv_time <= play_time:
        sum_value = dp[dp_count + adv_time] - dp[dp_count]
        if sum_value > max_value:
            max_value = sum_value
            answer = dp_count + 1
        dp_count += 1
    return transfer_second_to_time(answer)
