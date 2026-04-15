n = int(input())
while n < 0:
    n = int(input())
n_inicial = n
f = 0
x, y = 1, 1

for i in range(2, n):
    f = x + y
    x, y = y, f
    
if n_inicial == 1:
    print(1)
elif n_inicial == 0:
    print(0)
else:
    print(y)