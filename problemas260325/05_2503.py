par = 0
impar = 0
pos = 0
neg = 0
n = 0

while n < 5:
    numero = int(input())
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    if numero > 0:
        pos += 1
    elif numero < 0:
        neg += 1
              
    n += 1

print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)")

