import sys

channel = int(sys.stdin.readline())
n = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))

ans = abs(channel-100)

for i in range(1000001):
    flag = True
    for j in str(i):
        if int(j) in broken:
            flag = False
            break
    if flag:
        ans = min(ans, len(str(i)) + abs(i - channel))
print(ans)