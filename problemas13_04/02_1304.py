x, y = map(int, input().split())
if y < x:
    x, y = y, x
um = 1
n = y
m = x

    
for i in range (1, y+1):
    print(i, end=" ")
    if i % x == 0:
        print()