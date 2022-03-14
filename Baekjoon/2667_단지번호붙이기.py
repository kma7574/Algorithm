import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
pMap = []
for _ in range(n):
    pMap.append(list(map(int, list(input()))))


def dfs(x, y, pMap, visited):
    global size

    visited[x][y] = 1
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1), ]  # 위, 왼쪽, 아래, 오른쪽
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or ny < 0 or nx > len(pMap) - 1 or ny > len(pMap) - 1:  # 지도 벗어남
            continue
        if pMap[nx][ny] == 0:  # 집이 아님
            continue
        if not visited[nx][ny]:  # 이동한 위치가 인접한 방문하지 않은 새로운 집
            size += 1
            dfs(nx, ny, pMap, visited)


def survey(pMap):
    global size

    visited = []  # 방문 여부 변수
    for i in range(n):
        visited.append([0 for j in range(n)])

    size_list = []  # 단지 사이즈를 저장할 변수
    for h in range(n):
        for w in range(n):
            if pMap[h][w] == 1 and visited[h][w] == 0:  # 이전에 방문하지 않은 새로운 집
                size = 1
                # visited[h][w] = 1
                dfs(h, w, pMap, visited)
                size_list.append(size)
    size_list.sort()
    return len(size_list), size_list


num_ans, ans_list = survey(pMap)
print(num_ans)
for ans in ans_list:
    print(ans)
