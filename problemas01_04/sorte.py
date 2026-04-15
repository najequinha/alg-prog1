n, x = map(int, input().split())
sorte = False

for i in range(n):
    y = int(input())
    if y == x:
        sorte = True

if sorte:
    print("Sorte")
    
else:
    print("Azar")
