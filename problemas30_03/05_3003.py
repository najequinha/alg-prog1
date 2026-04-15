maior = 0
anterior = 0
pos = 0

for i in range(1, 51):
    n = int(input())
    if n > anterior and n > maior:
        maior = n
        pos = i
    anterior = n
    
print(f"{maior}\n{pos}")