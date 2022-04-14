import copy
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

comb = list(combinations(range(N * M), 3))  # 벽을 세울 수 있는 모든 경우의 수

direction = [(-1, 0), (0, -1), (1, 0), (0, 1), ]  # 위, 왼쪽, 아래, 오른쪽


# 좌표 반환 ex) 7x7맵에서 11은 (1,6)
def get_coordinate(number):
    return number // M, number % M


# 바이러스 확산
def spread_virus(x, y):
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx < N and 0 <= ny < M:  # 좌표가 연구소안에 포함되고
            if tmp_data[nx][ny] == 0:  # 빈칸이라면
                tmp_data[nx][ny] = 2  # 바이러스 확산
                spread_virus(nx, ny)
    return


# 바이러스 모두 확산된후 안전영역 계산
def get_score(pMap):
    score = 0
    for i in range(N):
        for j in range(M):
            if pMap[i][j] == 0:
                score += 1
    return score


ans = 0
for c in comb:
    tmp_data = copy.deepcopy(data)
    wall_count = 0  # 벽을 3개 다 세웠는지 확인하는 변수
    for k in c:
        x, y = get_coordinate(k)
        if tmp_data[x][y] != 0:  # 이미 벽이거나 바이러스라면
            break
        tmp_data[x][y] = 1  # 매 조합마다 3개씩 벽 세우기
        wall_count += 1

    if wall_count == 3:  # 벽을 3개 세운 경우에만 계산
        for i in range(N):
            for j in range(M):
                if tmp_data[i][j] == 2:
                    spread_virus(i, j)
        tmp_ans = get_score(tmp_data)
        if ans < tmp_ans:
            ans = tmp_ans

print(ans)