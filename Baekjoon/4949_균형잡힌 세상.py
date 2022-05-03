import sys

data = []
while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    else:
        data.append(s)

for sentence in data:
    stack = []
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')