import sys
N = int(sys.stdin.readline())
arr_N = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
arr_M = list(map(int,sys.stdin.readline().split()))

def solution(x, data):
    '''
    입력받은 숫자가 리스트에 있나 없나를 찾아서 반환(0,1)
    '''
    ''' 시간초과
    if len(data) == 1:
        if data[0] == x:
            return 1
        else:
            return 0
    mid = len(data) // 2
    if x < data[mid]:
        return solution(x, data[:mid])
    else:
        return solution(x, data[mid:])
    '''
    left = 0
    right = len(data)-1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == x:
            return 1
        
        if x < data[mid]:
            right = mid-1
        else:
            left = mid+1
    return 0

for i in arr_M:
    print(solution(i,arr_N))
