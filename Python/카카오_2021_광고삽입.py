'''미완성'''

def transfer_time_to_second(time_str):
    h, m, s = map(int, time_str.split(':'))

    h *= 60 * 60
    m *= 60

    return h + m + s


def transfer_second_to_time(second):
    h = second % 60 

def solution(play_time, adv_time, logs):
    answer = 0

    play_time = transfer_time_to_second(play_time)
    adv_time = transfer_time_to_second(adv_time)

    dp = [0] * play_time

    max_value = 0

    for log in logs:
        start, end = log.split('-')
        start = transfer_time_to_second(start)
        end = transfer_time_to_second(end)

        dp[start] += 1
        dp[end] -= 1

    dp_count = 0
    while dp_count + adv_time <= play_time:
        sum_value = sum(dp[dp_count: dp_count + adv_time])
        if sum_value > max_value:
            max_value = sum_value
            answer = dp_count
        dp_count += 1


    return answer


logs_ = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution("02:03:55", "00:14:15", logs_))
