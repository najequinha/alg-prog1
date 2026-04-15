n = int(input())
cont = 0
for i in range(1, n+1):
    q = i ** 2
    c = i ** 3
    print(i, q, c)
    for j in range(1):
        q += 1
        c += 1
        print(i, q, c)