x = int(input())
z = int(input())

while z <= x:
    z = int(input())
    
soma = 0
y = 0
atual = x

while soma <= z:
    soma += atual
    atual += 1
    y += 1

print(y)