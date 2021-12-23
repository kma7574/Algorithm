import sys
n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

p = 0
for num in numbers:
    error = False
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error = True # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
                break
        if error is False:
            p += 1  # error가 없으면 소수.
print(p)