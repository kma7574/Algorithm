import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]  # 계산 편리 위해 0번째 인덱스는 더미로 설정
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1


# print(graph)


def dfs(g, v):
    dfs_visit[v] = 1
    print(v, end=" ")
    for i in range(1, N + 1):
        if dfs_visit[i] == 0 and g[v][i] == 1:
            dfs(g, i)


def bfs(g, v):
    q = deque()
    q.append(v)
    bfs_visit[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if bfs_visit[i] == 0 and g[v][i] == 1:
                q.append(i)
                bfs_visit[i] = 1


dfs_visit = [0] * (N + 1)
bfs_visit = [0] * (N + 1)
dfs(graph, V)
print()
bfs(graph, V)
