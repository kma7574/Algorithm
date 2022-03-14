import sys
import math
from itertools import combinations

N = int(sys.stdin.readline())
mp, mf, ms, mv = map(int, sys.stdin.readline().split())
data = [[0,0,0,0,0]]
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

min_cost = math.inf
min_material = tuple(range(1, N + 1))
material = range(1, N + 1)  # 재료 번호 리스트


def tp_to_str(tp):
    num = ''
    for i in tp:
        num += str(i)
    return num


def min_material_to_str(num):
    num = str(num)
    rt = ''
    for i in num:
        rt += i + ' '
    return rt.rstrip()


for cnt in range(1, N + 1):
    for comb in combinations(material, cnt):
        # print(comb)
        p = f = s = v = c = 0
        for i in comb:  # 선택한 재료 조합의 총 영양소 체크
            p += data[i][0]
            f += data[i][1]
            s += data[i][2]
            v += data[i][3]
            c += data[i][4]

        if p >= mp and f >= mf and s >= ms and v >= mv:
            if c < min_cost:
                min_cost = c
                min_material = comb
            elif c == min_cost:  # 사전식 배열 통해 빠른 걸로
                # if tp_to_str(comb) < min_material:
                #     min_material = tp_to_str(comb)
                # if comb < min_material:
                #     min_material = comb
                min_material = sorted((min_material, comb))[0]

if min_cost == math.inf:
    print(-1)
else:
    print(min_cost)
    # print(min_material_to_str(min_material))
    print(*min_material)