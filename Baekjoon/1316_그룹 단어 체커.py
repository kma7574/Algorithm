import sys
n = int(sys.stdin.readline())
ans= 0

for _ in range(n):
    s = sys.stdin.readline()
    if list(s) == sorted(s, key=s.find):
        # key=s.find :문자열의 왼쪽부터 모든문자들이 해당 리스트에서 몇번째로 발견되었는지 순으로 정렬
        # ex) aacdcbacdb -> aaacccddbb
        ans += 1
    print(s, *sorted(s, key=s.find))
print(ans)