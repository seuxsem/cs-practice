a, op, b = map(str.strip, input().split(' '))
a, b = map(int, (a, b))

if op == '+':
    print(a + b)

if op == '*':
    print(a * b)