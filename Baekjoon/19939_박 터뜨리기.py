import sys

N, K = map(int, sys.stdin.readline().split())


def sum_k(k):
    return k * (k + 1) // 2


ans = 0
if N < sum_k(K):  # 1,2,3,4,5.. 이런식으로 분배해도 불가능
    ans = -1
else:
    if (N - sum_k(K)) % K == 0:  # 1,2,3,4,5.. 이런식으로 분배했다 치고 남은공의 개수가 바구니와 배수관계면 가장많은 바구니 공개수는 K이고 적은 바구니 공개수는 1
        ans = K - 1
    else: # 배수관계가 아니면 (N - sum_k(K)) % K 개의 공을 가장많은 바구니부터 하나씩 더해가면 되므로 (k+1) -1 = k
        ans = K
print(ans)
