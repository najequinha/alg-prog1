n = int(input())
contador = 0
while n < 1 or n > 1000000:
    n = int(input())

for i in range(1, n+1, 1):
    if n % i == 0:
        contador += 1
if contador == 2:
    print("Primo")
else:
    print("Composto")