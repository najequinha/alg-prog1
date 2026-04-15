n = int(input())
potencia = 1
s = 0

while n > 0:
    resto = n % potencia
    n = n // potencia
    print(resto)
    potencia *= 10
    s += 1
    
print(s)
for i in range(s, 0, -1):
    print(i)
    