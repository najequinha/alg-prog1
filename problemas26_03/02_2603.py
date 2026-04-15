n = int(input())
pot = 1
soma = 0

while n > 0:
    resto = n % 10
    soma += resto * pot
    pot *= 2
    n = n // 10
    
print(soma)