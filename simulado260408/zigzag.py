n = int(input())
m = 1
p = n

for i in range(1, n+1):
    if i % 2 ==1:
        for j in range(m, p+1):
            print(j, end=" ")
    else:
        for j in range(p, m-1, -1):
            print(j, end=" ")
    print()    
    m+=n
    p+=n