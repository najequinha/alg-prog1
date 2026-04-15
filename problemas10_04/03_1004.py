t = int(input())

while t < 1 or t > 3000:
    t = int(input())
    
for i in range(t):
    pa, pb, g1, g2 = input().split()
    pa, pb = int(pa), int(pb)
    g1, g2 = float(g1), float(g2)

    tax1 = g1 / 100
    tax2 = g2 / 100
    anos = 0
    final_a = pa
    final_b = pb
    
    while final_a <= final_b:
        crescimento_a = int(final_a * tax1)
        final_a += crescimento_a
        crescimento_b = int(final_b * tax2)
        final_b += crescimento_b
        anos+=1
        if (anos) > 100:
            print("Mais de 1 seculo")
            break
    if anos <= 100:
        print(f"{anos} anos.")
