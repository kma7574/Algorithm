import sys
data = sys.stdin.readline().rstrip()

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia:
    data = data.replace(i, '@')
print(len(data))
        