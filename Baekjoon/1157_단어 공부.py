import sys
from collections import Counter

word = sys.stdin.readline().rstrip()
dict = Counter(word.upper())
result = []

for i in dict.keys():
    if dict[i] == max(dict.values()):
        result.append(i)

if len(result) > 1:
    print("?")
else:
    print(result[0])
