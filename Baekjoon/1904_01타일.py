import sys

n = int(sys.stdin.readline())


def count_tile(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    tmp_count = [0, 1, 2]
    for i in range(3, x + 1):
        tmp_count.append((tmp_count[-1] + tmp_count[-2]) % 15746)
    return tmp_count[-1]


print(count_tile(n) % 15746)

# 메모리 초과
# def count_tile(x):
#     if x == 1:
#         return 1
#     elif x == 2:
#         return 2
#     tmp_count = [0, 1, 2]
#     for i in range(3, x + 1):
#         tmp_count.append(tmp_count[-1] + tmp_count[-2])
#     return tmp_count[-1] % 15746
