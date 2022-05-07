import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

answer = ''


def quad_tree(x, y, n):
    global answer
    check = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != check:
                answer += '('  # 현재 영상을 4등분하므로 4등분한 영상의 결과를 괄호로 묶어준다.
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                answer += ')'
                return
    answer += str(check)
    return


quad_tree(0, 0, N)
print(answer)