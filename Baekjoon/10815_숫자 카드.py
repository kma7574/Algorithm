import sys

N = int(sys.stdin.readline())
my_card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_card = list(map(int,sys.stdin.readline().split()))
my_card = sorted(my_card)
answer = []

# 브루트 포스는 시간초과이므로, 이진탐색을 통해서 진행
def binary_search(card, num, start, end):
    while start <= end:
        mid = (start + end) // 2

        if card[mid] == num:
            return 1
        elif card[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for c in check_card:
    if binary_search(my_card, c, 0, len(my_card)-1):
        print(1, end=' ')
    else:
        print(0, end=' ')