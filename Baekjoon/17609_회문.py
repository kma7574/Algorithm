import sys

T = int(sys.stdin.readline().strip())


def palindrome_check(_word, _left, _right):
    while _left < _right:
        if word[_left] == word[_right]:
            _left += 1
            _right -= 1
        else:
            return False
    return True


def pseudo_check(_word, _left, _right):
    while _left < _right:
        if word[_left] == word[_right]:
            _left += 1
            _right -= 1
        else:
            check1 = palindrome_check(_word, _left + 1, _right)
            check2 = palindrome_check(_word, _left, _right - 1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0


for _ in range(T):
    word = sys.stdin.readline().strip()
    left = 0
    right = len(word) - 1
    ans = pseudo_check(word, left, right)
    print(ans)
