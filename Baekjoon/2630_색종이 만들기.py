import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

white, blue = 0, 0


def check_color(x, y, n):
    global white, blue
    check = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != check:
                check_color(x, y, n//2)
                check_color(x, y+n//2, n//2)
                check_color(x+n//2, y, n//2)
                check_color(x+n//2, y+n//2, n//2)
                return
    if check == 0:
        white += 1
    else:
        blue += 1
    return


check_color(0, 0, N)
print(white)
print(blue)
