import sys
A, B = map(str, sys.stdin.readline().split())

numbers = dict()
count = 0
answer = [0, 0]
# 1부터 저장
for i in range(0, 10):
    numbers[str(i)] = i

# a부터 저장
for i in range(26):
    numbers[chr(97+i)] = i+10

a_max = max(list(A))
b_max = max(list(B))


def trans_notation(string, notation):
    num = 0
    for i in range(len(string)):
        num += ((int(notation)**i) * numbers[string[-1-i]])
    return num


for i in range(numbers[a_max]+1, 37):
    for j in range(numbers[b_max]+1, 37):
        if i == j:
            continue
        if trans_notation(A, i) == trans_notation(B, j):
            if trans_notation(A, i) >= 2**63:
                continue
            answer[0] = i
            answer[1] = j
            count += 1

if count == 0:
    print("Impossible")
elif count > 1:
    print("Multiple")
elif count == 1:
    print(trans_notation(A, answer[0]), answer[0], answer[1])
