import sys

N, K = map(int, sys.stdin.readline().split())
data = sys.stdin.readline().strip()

"""
HHHHHPPPPPHPHPHPHHHP K=2
H_idx: [1,2,3,4,5,11,13,15,17,18,19]
P_idx: [6,7,8,9,10,12,14,16,20]
"""
H_idx, P_idx = [], []
for i in range(len(data)):
    if data[i] == 'H':
        H_idx.append(i)
    else:
        P_idx.append(i)

ans = 0
h, p = 0, 0
while True:
    if (h >= len(H_idx)) or (p >= len(P_idx)):
        break

    if abs(H_idx[h] - P_idx[p]) <= K:
        ans += 1
        h += 1
        p += 1
    else:
        if H_idx[h] < P_idx[p]:
            h += 1
        else:
            p += 1

print(ans)
