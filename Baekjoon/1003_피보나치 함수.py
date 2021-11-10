import sys
T = int(sys.stdin.readline())
data = []
for i in range(T):
    data.append(int(sys.stdin.readline()))
# print(data)


for i in range(T):
    cnt0 = [1, 0] # 0이 몇번 호출되었는지 카운트
    cnt1 = [0, 1] # 1이 몇번 호출되었는지 카운트
    if data[i] == 0:
        print(f'{cnt0[0]} {cnt1[0]}')
    elif data[i] == 1:
        print(f'{cnt0[1]} {cnt1[1]}')
    else:
        for j in range(2, data[i]+1):
            cnt0.append(cnt0[j-2] + cnt0[j-1])
            cnt1.append(cnt1[j-2] + cnt1[j-1])
        print(f'{cnt0[-1]} {cnt1[-1]}')