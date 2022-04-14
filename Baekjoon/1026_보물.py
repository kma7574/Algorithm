import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

S = 0

"""
꼼수 쓰면 빠르게 풀림
"""
# A = sorted(A, reverse=True)
# B = sorted(B, reverse=False)
# for i in range(N):
#     S += A[i] * B[i]
# print(S)

"""
문제 조건 지키며 풀기
"""
for i in range(N):
    S += max(A) * min(B)
    A.pop(A.index(max(A)))
    B.pop(B.index(min(B)))
print(S)