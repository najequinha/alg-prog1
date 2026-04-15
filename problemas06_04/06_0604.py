r = float(input())
n = int(input())
potencia = 1

for i in range(n):
    potencia *= r

print(f"{potencia:.2f}")