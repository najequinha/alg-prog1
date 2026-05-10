s = float(input())

if s >= 0 and s <= 400:
    n_s = s + s * 0.15
    d_s = n_s - s
    r = 15
    print(f"Novo salario: {n_s:.2f}\nReajuste ganho: {d_s:.2f}\nEm percentual: {r} %")
elif s >= 400.01 and s <= 800:
    n_s = s + s * 0.12
    d_s = n_s - s
    r = 12
    print(f"Novo salario: {n_s:.2f}\nReajuste ganho: {d_s:.2f}\nEm percentual: {r} %")
elif s >= 800.01 and s <= 1200:
    n_s = s + s * 0.10
    d_s = n_s - s
    r = 10
    print(f"Novo salario: {n_s:.2f}\nReajuste ganho: {d_s:.2f}\nEm percentual: {r} %")
elif s >= 1200.01 and s <= 2000:
    n_s = s + s * 0.07
    d_s = n_s - s
    r = 7
    print(f"Novo salario: {n_s:.2f}\nReajuste ganho: {d_s:.2f}\nEm percentual: {r} %")
else:
    if  s > 2000:
        n_s = s + s * 0.04
        d_s = n_s - s
        r = 4
        print(f"Novo salario: {n_s:.2f}\nReajuste ganho: {d_s:.2f}\nEm percentual: {r} %")

