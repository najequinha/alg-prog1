x = float(input())
k = int(input())

cos = 1
sinal = -1

for i in range(2, k+1, 2):
    fat = 1
    for j in range(1, i+1):
        fat *= j

    calc = (x**i)/fat

    cos += sinal * calc
    sinal *= -1

print(f"{cos:.4f}")
