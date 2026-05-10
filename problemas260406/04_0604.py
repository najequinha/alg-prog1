n = int(input())
for i in range(n):
    s = 0
    x, y = map(int, input().split())
    if x > y:
        y, x = x, y
    for j in range(x+1, y, 1):
        if j % 2 != 0:
            s += j
    print(s)
