import sys
from collections import deque

test = int(sys.stdin.readline())


def custom_printer(arr, check_arr):
    count = 1
    while True:
        if arr[0] == max(arr) and check_arr[0]:
            return count
        elif arr[0] == max(arr) and check_arr[0] is False:
            count += 1
            arr.popleft()
            check_arr = check_arr[1:]
        else:
            tmp = arr.popleft()
            arr.append(tmp)
            tmp = check_arr[0]
            check_arr = check_arr[1:]
            check_arr.append(tmp)


for _ in range(test):
    N, M = map(int, sys.stdin.readline().split())
    important = deque(list(map(int, sys.stdin.readline().split())))
    check = [False] * N
    check[M] = True
    print(custom_printer(important, check))
    
