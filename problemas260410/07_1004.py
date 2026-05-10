x = float(input())
n = int(input())
soma = 0
cons = 1 

for i in range(1, n+1):
    fat = 1
    for j in range(1, i+1):
        fat *= j
    calc = (x**i)/fat
    soma = soma + calc
    
cons += soma

print(f"{cons:.4f}")