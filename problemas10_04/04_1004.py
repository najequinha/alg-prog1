n = int(input())

while n < 1 or n > 20:
    n = int(input())
    
while n > 0:
    x = int(input())
    s = 0
    while x < 1 or x > (10**8):
        x = int(input())
        
    for i in range(1, x, 1):
        if x % i == 0:
            s += i
            print(i, s)
    if s == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
    n -= 1
