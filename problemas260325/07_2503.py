x = int(input())

n = x + 11

while x <= n:
    if x % 2 != 0:
        print(x)
    else:
        x = x
    x += 1