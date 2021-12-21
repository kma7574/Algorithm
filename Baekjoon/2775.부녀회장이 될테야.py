import sys
T = int(sys.stdin.readline())
for i in range(T):
    k = int(sys.stdin.readline()) #층
    n = int(sys.stdin.readline()) #호
    
    people = [[x+1 for x in range(n)]]
    for i in range(1,k+1):
        floor = [1] # 1호의 인구수는 항상 1명
        for j in range(1, n):
            # 현재위치 인구수는 전집 인구수와 바로아랫층 인구수의 합
            floor.append(people[-1][j] + floor[-1])
        people.append(floor)
    print(people[-1][-1])
            