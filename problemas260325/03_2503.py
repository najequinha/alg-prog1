i = 1
n = 0
m = 0

while i <= 6:
    n_ = float(input())
    if n_ > 0:
        n += 1
        m += n_
    else:
        n = n
    i += 1

print(f"{n} valores positivos")
media = m/n
print(f"{media:.1f}")
