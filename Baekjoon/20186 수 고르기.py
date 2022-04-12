import sys

N, K = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort(reverse=True)
print(sum(data[:K]) - sum(range(K)))