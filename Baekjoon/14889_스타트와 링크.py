import sys
from itertools import combinations

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

member = list(range(n))
team_list = list(combinations(member, n//2))
gap = 999999

for team1 in team_list:
    team2 = list(set(member) - set(team1))
    team1_pair = list(combinations(team1, 2))
    team2_pair = list(combinations(team2, 2))
    #  print(f'team1:{team1_pair}, team2:{team2_pair}')  # team1:[(0, 3), (0, 4), (3, 4)], team2:[(1, 2), (1, 5), (2, 5)]
    stat1 = 0
    stat2 = 0
    for i in range(len(team1_pair)):
        stat1 += (data[team1_pair[i][0]][team1_pair[i][1]] + data[team1_pair[i][1]][team1_pair[i][0]])
        stat2 += (data[team2_pair[i][0]][team2_pair[i][1]] + data[team2_pair[i][1]][team2_pair[i][0]])
    if gap > abs(stat1 - stat2):
        gap = abs(stat1 - stat2)
print(gap)


