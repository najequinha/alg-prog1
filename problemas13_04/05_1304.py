n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    p = x+(y*2)
    soma = 0
    for j in range(x, p):
        if j % 2 != 0:
            soma += j
    print(soma)