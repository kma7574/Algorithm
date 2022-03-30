import sys

n = int(sys.stdin.readline())


def maximum_subarray(x):
    tmp_sum = x[0]
    ans = x[0]

    for i in range(1, len(x)):
        tmp_sum = max(x[i], tmp_sum + x[i])
        ans = max(tmp_sum, ans)
    return ans


for i in range(n):
    k = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    print(maximum_subarray(data))
