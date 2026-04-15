#Ana Julia de Freitas de Arruda
n = int(input())
resultado = 0
potencia = 1

while n < 0:
    n = int(input())

while n > 0:
    tern = n % 3
    n = n // 3
    resultado += tern * potencia
    potencia *= 10
    
print(f"\n{resultado}")
