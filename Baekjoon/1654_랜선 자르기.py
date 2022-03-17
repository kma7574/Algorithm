import sys

K, N = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for i in range(K)]  # [802, 743, 457, 539]

min_len = 1
max_len = sum(data) // len(data)

while min_len <= max_len:
    mid = (min_len + max_len) // 2
    cnt = 0
    for i in data:
        cnt += (i // mid)

    if cnt >= N:  # N개보다 더 많이 나왔다는것은 더 길게 만들수도 있다는것
        min_len = mid + 1
    else:  # N개보다 적게 만들어졌으니 길이를 줄여 개수를 늘려야 한다.
        max_len = mid - 1
print(max_len)


# """
# 시간초과
# """
# ideal = sum(data) // len(data)  # 이상적으로 만들 수 있는 가장긴 랜선
# cnt = 0
# while True:
#     for i in data:
#         cnt += (i // ideal)
#     if cnt >= N:
#         break
#     else:
#         ideal -= 1
#         cnt = 0
#
# print(ideal)
