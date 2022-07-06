import sys
import math

w, h, x, y, p = map(int,sys.stdin.readline().split())
ans = 0

def cal_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


for _ in range(p):
    a, b = map(int,sys.stdin.readline().split())
    # 일단 사각형안에 있는지 조사후
    if x <= a <= x+w and y <= b <= y+h:
        ans += 1
    # 양쪽의 반원에 포함되어있는지 확인(반지름과의 거리)
    elif cal_distance(x, y+h/2, a, b) <= h/2 or cal_distance(x+w, y+h/2, a, b) <= h/2:
        ans += 1

        
print(ans)