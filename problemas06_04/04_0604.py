s = 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if y > x:
        y, x = x, y
    for j in range(x-1, y, -1):
        if j % 2 != 0:
            s += j
        else:
            s = s
    print(s)