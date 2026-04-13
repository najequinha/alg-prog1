n = int(input())
pot = 1
binario = 0

while n > 0:
    m = n % 2
    n = n // 2
    binario += (m * pot)
    pot *= 10
print(binario)