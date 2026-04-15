#x, y = map(int, input().split)
x = int(input())
y = int(input())

s = 0

if x > y:
    x -= 1
    y += 1
    while y <= x:
        if y % 2 != 0:
            s += y
        else:
            s = s
        y += 1
    print(s)

else:
    x += 1
    y -= 1
    while x <= y:
        if x % 2 != 0:
            s += x
        else:
            s = s
        x += 1
    print(s)
        
