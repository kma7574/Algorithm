import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().strip())))

direction = [(-1, 0), (0, -1), (1, 0), (0, 1), ]  # 위, 왼쪽, 아래, 오른쪽

step = 1


def bfs():
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 1:
                q.append((nx, ny))
                data[nx][ny] = data[x][y] + 1
    return data[-1][-1]


print(bfs())
