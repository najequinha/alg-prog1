x = int(input())
y = int(input())
s = 0
if x > y:
    if x < 0:
        x = x + 1
    else:
        x -= 1
    if y < 0:
        y = y + 1
    else:
        y -= 1
    while x > y:
        if y % 2 != 0:
            s += y
        else:
            s = s
        x -= 1
    print(s)
    
else:        
    if x < 0:
        x = x - 1
    else:
        x += 1
    if y < 0:
        y = y - 1
    else:
        y += 1
    x, y = y, x
    while x > y:
        if y % 2 != 0:
            s += y
        else:
            s = s
        x =- 1
    print(s)

