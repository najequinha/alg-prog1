n = int(input())
s0 =  0
sim = False
nao = False
while n < 1:
    n = int(input())
for i in range(n):
    s1 = int(input())
    if s1 == s0:
        sim =  True
    else:
        nao = True
    s0 = s1

if sim == True:
    print("Sim")
else:
    print("Nao")
