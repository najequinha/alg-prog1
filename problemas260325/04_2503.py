i = 0
n = 0

while n < 5:
    numero = int(input())
    if numero % 2 == 0:
        i += 1
    else:
        i = i
    n += 1

print(f"{i} valores pares")
