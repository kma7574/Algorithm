import sys

data = list(map(int, sys.stdin.readline().split()))
data = [str(x) for x in data]
data = ''.join(data)


def calc_clock_num(x: str) -> int:
    """
    시계수 찾기
    """
    clock_num = int(''.join(x))
    for i in range(len(x)):
        tmp = int(x[i:] + x[:i])
        if clock_num > tmp:
            clock_num = tmp
    return clock_num


ans = 0
"""
최소시계수부터 구한시계수까지의 개수를 구함
"""
for i in range(1111, int(calc_clock_num(data)) + 1):
    if calc_clock_num(str(i)) == i:  # 시계수가 맞는지 검사
        ans += 1  # 맞으면 구한 시계수보다 작은 시계수가 존재한다는 것이므로 1 증가
print(ans)

'''
찾은 시계수보다 작은 시계수가 얼마나 있는가
'''
# print(list(str(clock_num)))
# ans = 0
# digit = [int(x) for x in str(clock_num)]
# print(digit)
# for j in range(len(digit)):
#     ans += (int(digit[j])-1) * 9**(len(data)-j-1)
# print(ans)
