import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    adj[src].append(dst)
    adj[dst].append(src)
for x in range(1, N+1):
    adj[x] = sorted(adj[x])

print(adj)
visited = [0] * (N+1)
nodes_cnt = [0] * (N+1)
order = 1  # 방문순서 체크 변수
stack = deque()
stack.append(R)


while stack:
    cur_node = stack.pop()
    visited[cur_node] = 1
    if nodes_cnt[cur_node] == 0:
        nodes_cnt[cur_node] = order
        order += 1

    for next_node in adj[cur_node]:
        if visited[next_node] == 0:
            stack.append(next_node)

print(*nodes_cnt[1:])