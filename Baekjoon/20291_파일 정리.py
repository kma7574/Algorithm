import sys
from collections import defaultdict

N = int(sys.stdin.readline())
extensions = defaultdict(int)

for i in range(N):
    file = sys.stdin.readline().strip()
    extension = file.split('.')[-1]  # 확장자 추출
    extensions[extension] += 1
# print(type(extensions))
extensions = dict(sorted(extensions.items()))  # 딕셔너리를 sorted 메소드로 정렬하면 반환값은 리스트 ㄷㄷ
extensions = dict(extensions)
for key, value in extensions.items():
    print(key, value)



