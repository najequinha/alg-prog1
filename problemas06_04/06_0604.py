r = float(input())
n = int(input())
potencia = r

for i in range(1, n, +1):
    potencia = potencia * r

print(f"{potencia:.2f}")