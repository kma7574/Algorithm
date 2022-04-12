import sys

num = sys.stdin.readline().strip()


def solution(data):
    length = len(data)

    start_list = [data[0], data[:2], data[:3]]  # 첫번째숫자가 한자리,두자리,세자리인경우
    for i in start_list:
        number = ''
        tmp = i

        while len(number) < length:
            number += tmp

            if number == data:
                return i, tmp
            tmp = str(int(tmp) + 1)

    return data, data


print(*solution(num))