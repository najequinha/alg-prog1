n = int(input())
x = 1
while x <= n:
    if x % 2 == 0:
        print(f"{x}^2 = {x**2}")
    else:
        x = x
    x +=1