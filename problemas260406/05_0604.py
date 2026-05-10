while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    if n > m:
        m, n = n, m
    s = 0
    for i  in range(n, m+1, +1):
        print(i, end=" ")
        s += i
    print(f"Sum={s}")
    