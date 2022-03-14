import sys
m = int(sys.stdin.readline())
# 리스트로 입력받아 문자열로 변환
sample = list(map(int,sys.stdin.readline().split()))
sample = tmp = [str(x) for x in sample]
sample = ''.join(sample)

data = []
n = int(sys.stdin.readline())
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp = [str(x) for x in tmp]
    tmp = ''.join(tmp)
    data.append(tmp)


def rev(x): # 1411433322 -> 4411123323
    """
    문자열 뒤집은 후, 그리는 방향을 반대로 return
    """
    x = ''.join(reversed(x))
    rev_num = ''
    for i in range(len(x)):
        if x[i] == '1':
            rev_num += '3'
        if x[i] == '2':
            rev_num += '4'
        if x[i] == '3':
            rev_num += '1'
        if x[i] == '4':
            rev_num += '2'
    return rev_num


ans = []
for i in range(len(data)):
    for j in range(len(data[i])):
        tmp = data[i][j:] + data[i][:j]  # 시작점을 바꾼 모양수열
        if tmp == sample or rev(tmp) == sample:  # 시작점만 바꿔서 동일하게 그릴 수 있거나 시작점, 그리는방향 모두 바꿔 그릴수 있거나
            ans.append(data[i])
            break

# 정답출력
print(len(ans))
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end=' ')
    print()