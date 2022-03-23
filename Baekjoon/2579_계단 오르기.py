import sys
n = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(n)]
score.insert(0, 0)  # 0번째 인덱스에 dummy 삽입(n번째 인덱스가 n번째 계단임)


def stair(data):
    if len(data) == 2:
        return data[1]
    elif len(data) == 3:
        return data[1] + data[2]
    tmp_sum = [0, data[1], data[1] + data[2]]  # 0,1,2번째 계단까지 올랐을 때 최고점
    for i in range(3, len(data)):
        tmp_sum.append(max(tmp_sum[i - 3] + data[i - 1] + data[i], tmp_sum[i - 2] + data[i]))
    return tmp_sum[-1]


print(stair(score))