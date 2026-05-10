n = int(input())
pot = 1
anterior = 0 
atual = n
soma = 0
while atual > 0:
    anterior = atual
    atual = atual // 10
    numero = anterior - (atual * 10)
    if numero % 2 == 0:
        numero *= pot
        soma+= numero
        pot*= 10
print(soma)